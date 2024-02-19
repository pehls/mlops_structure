"""Console script for mlops_structure."""

import fire


def help() -> None:
    print("mlops_structure")
    print("=" * len("mlops_structure"))
    print("MLOps full structure for llm/ml, do")


def main() -> None:
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
