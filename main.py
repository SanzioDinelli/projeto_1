import argparse
from pathlib import Path


def create_projects(num_projects: int = 5):
    """
    Cria múltiplas pastas na pasta pai do projeto atual.
    
    Args:
        num_projects: Número de projetos a criar (padrão: 5)
    """
    # Pega a pasta pai do projeto atual
    current_dir = Path(__file__).parent
    parent_dir = current_dir.parent
    
    # Cria as pastas projeto_2, projeto_3, etc.
    for i in range(2, num_projects + 1):
        project_folder = parent_dir / f"projeto_{i}"
        project_folder.mkdir(exist_ok=True)
        print(f"✓ Pasta criada: {project_folder}")


def main():
    parser = argparse.ArgumentParser(
        description="Cria múltiplas pastas de projeto na pasta pai"
    )
    parser.add_argument(
        "-n", "--num-projects",
        type=int,
        default=5,
        help="Número de projetos a criar (padrão: 5)"
    )
    
    args = parser.parse_args()
    
    create_projects(num_projects=args.num_projects)
    print("\nTodas as pastas foram criadas com sucesso!")


if __name__ == "__main__":
    main()
