from dataclasses import dataclass

PERCENT_RATE = 0.01  # 1%


@dataclass
class Department:
    name: str
    sales_amount: float
    employees_count: int

    @property
    def bonus_pool(self) -> float:
        return self.sales_amount * PERCENT_RATE

    @property
    def payout_per_employee(self) -> float:
        return self.bonus_pool / self.employees_count


def read_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Введите целое число больше 0.")


def read_non_negative_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            value = float(raw)
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Введите число 0 или больше.")


def read_departments() -> list[Department]:
    departments_count = read_positive_int("Сколько отделов нужно посчитать? ")
    departments: list[Department] = []

    for index in range(1, departments_count + 1):
        print(f"\nОтдел #{index}")
        name = input("Название отдела: ").strip() or f"Отдел {index}"
        sales_amount = read_non_negative_float("Сумма продаж отдела: ")
        employees_count = read_positive_int("Количество людей в отделе: ")

        departments.append(
            Department(
                name=name,
                sales_amount=sales_amount,
                employees_count=employees_count,
            )
        )

    return departments


def print_report(departments: list[Department]) -> None:
    print("\n=== Результат расчёта ===")
    total_sales = 0.0
    total_bonus = 0.0

    for department in departments:
        total_sales += department.sales_amount
        total_bonus += department.bonus_pool

        print(f"\n{department.name}:")
        print(f"  Сумма продаж: {department.sales_amount:,.2f}")
        print(f"  1% от продаж: {department.bonus_pool:,.2f}")
        print(f"  Людей в отделе: {department.employees_count}")
        print(f"  Выплата на 1 человека: {department.payout_per_employee:,.2f}")

    print("\n--- Итого ---")
    print(f"Общая сумма продаж: {total_sales:,.2f}")
    print(f"Общий фонд (1%): {total_bonus:,.2f}")


def main() -> None:
    print("Расчёт зарплаты от 1% продаж отдела")
    print("Формула: сумма продаж отдела * 1% / количество людей в отделе")

    departments = read_departments()
    print_report(departments)


if __name__ == "__main__":
    main()
