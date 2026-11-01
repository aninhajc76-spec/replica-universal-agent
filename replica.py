#!/usr/bin/env python3
"""Ferramenta local para explorar o Agente Replica Universal (stdlib somente)."""
from __future__ import annotations
import argparse
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
MODULES = (
    'recon', 'architect', 'design', 'build', 'backend', 'test', 'diff',
    'entrepreneur', 'brand', 'launch', 'deploy'
)


def skills():
    return {name: ROOT / 'skills' / ('replica-' + name) / 'SKILL.md' for name in MODULES}


def read(path):
    return path.read_text(encoding='utf-8')


def prompt(name):
    common = read(ROOT / 'PROMPT_UNIVERSAL.md')
    if not name:
        return common
    return (common + '\n\n---\n\n# ETAPA SELECIONADA: /replica-' + name + '\n\n'
            + read(skills()[name]))


def validate():
    errors=[]
    for required in ('LICENSE','NOTICE.md','README.md','AGENTS.md',
                     'CLAUDE.md','GEMINI.md','PROMPT_UNIVERSAL.md',
                     '.github/copilot-instructions.md','.cursor/rules/replica.mdc'):
        if not (ROOT/required).is_file(): errors.append('Ausente: '+required)
    for name, path in skills().items():
        if not path.is_file():
            errors.append('Skill ausente: '+str(path)); continue
        contents=read(path)
        if not re.match(r'^---\s*\nname:\s*replica-'+re.escape(name)+r'\s*\n',contents):
            errors.append('Frontmatter inválido: '+name)
        if 'description:' not in contents[:2000]:
            errors.append('Sem descrição: '+name)
    return errors


def initialize(dest):
    base = dest.expanduser().resolve()/'replica'
    base.mkdir(parents=True,exist_ok=True)
    templates = {
        'recon.md': ROOT/'skills/replica-recon/recon-map.md',
        'features.csv': ROOT/'skills/replica-recon/features.csv',
        'architecture.md': ROOT/'skills/replica-architect/architecture.md',
        'test-plan.md': ROOT/'skills/replica-test/test-plan.md',
        'bugs.md': ROOT/'skills/replica-test/bug-report.md',
    }
    added=[]; skipped=[]
    for filename, source in templates.items():
        target=base/filename
        if target.exists():
            skipped.append(filename)
        elif source.is_file():
            target.write_bytes(source.read_bytes())
            added.append(filename)
        else:
            raise FileNotFoundError('Modelo indisponível: '+str(source))
    return base, added, skipped


def main(argv=None):
    parser=argparse.ArgumentParser(description='Replica Universal — CLI sem API de IA')
    commands=parser.add_subparsers(dest='command',required=True)
    commands.add_parser('list',help='Mostrar módulos')
    p=commands.add_parser('prompt',help='Gerar prompt para qualquer IA')
    p.add_argument('module',nargs='?',choices=MODULES)
    p.add_argument('--output',help='Gravar prompt em arquivo, sem sobrescrever')
    q=commands.add_parser('init',help='Criar arquivos iniciais no projeto')
    q.add_argument('project',help='Diretório do projeto')
    commands.add_parser('check',help='Validar arquivos e skills locais')
    args=parser.parse_args(argv)
    if args.command=='list':
        for name in MODULES: print('/replica-'+name)
    elif args.command=='prompt':
        value=prompt(args.module)
        if args.output:
            outfile=Path(args.output)
            try:
                with outfile.open('x',encoding='utf-8') as out: out.write(value)
            except FileExistsError:
                parser.error('O arquivo já existe: '+str(outfile))
            print('Prompt salvo em: '+str(outfile))
        else:
            print(value)
    elif args.command=='init':
        base,added,skipped=initialize(Path(args.project))
        print('Pasta:',base)
        print('Criados:',', '.join(added) or 'nenhum')
        print('Preservados:',', '.join(skipped) or 'nenhum')
    elif args.command=='check':
        errors=validate()
        for e in errors: print('ERRO:',e,file=sys.stderr)
        if not errors: print('OK — 11 skills e arquivos essenciais válidos')
        return 1 if errors else 0
    return 0

if __name__=='__main__':
    sys.exit(main())
