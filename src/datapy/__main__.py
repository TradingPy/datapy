"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Datapy."""


if __name__ == "__main__":
    main(prog_name="datapy")  # pragma: no cover
