from pathlib import Path

from models.customers import (
    Customer,
    WaterCompany,
)

# Default data file
DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "customers.txt"
)

# File header
FILE_HEADER = (
    "id|name|phone|district|category|barrels|bill"
)


def _is_column_header_line(line: str) -> bool:

    return (
        line.strip().lower().replace(" ", "")
        == FILE_HEADER.lower().replace(" ", "")
    )


def load_company(
    path: Path,
    company: WaterCompany,
) -> None:

    company.clear()

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            for raw in f:

                line = raw.strip()

                if (
                    not line
                    or line.startswith("#")
                    or line.startswith("Columns:")
                ):
                    continue

                if _is_column_header_line(line):
                    continue

                parts = line.split("|")

                # Supports both old and new files
                if len(parts) < 6:
                    continue

                cid = parts[0].strip()
                name = parts[1].strip()
                phone = parts[2].strip()
                district = parts[3].strip()
                category = parts[4].strip()

                try:
                    barrels = int(parts[5])

                except ValueError:
                    continue

                company.add(
                    Customer(
                        cid,
                        name,
                        phone,
                        district,
                        category,
                        barrels,
                    )
                )

    except FileNotFoundError:
        pass


def save_company(
    path: Path,
    company: WaterCompany,
) -> None:

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    lines = [
        "Columns: pipe-separated rows after the header line\n",
        f"{FILE_HEADER}\n",
    ]

    for c in company.all():

        lines.append(
            f"{c.customer_id}|"
            f"{c.name}|"
            f"{c.phone}|"
            f"{c.district}|"
            f"{c.category}|"
            f"{c.barrels}|"
            f"{c.calculate_bill():.2f}\n"
        )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        f.writelines(lines)