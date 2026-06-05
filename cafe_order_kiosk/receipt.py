from cafe_order_kiosk.utils import format_money


def print_receipt(order):
    print("\n" + "=" * 30)
    print("        영수증")
    print("=" * 30)

    print(f"주문번호: {order.id}")

    for item in order.items:
        print(
            f"{item.name} x{item.quantity} "
            f"{format_money(item.line_total)}"
        )

    print("-" * 30)
    print(f"총 금액: {format_money(order.total)}")
    print("=" * 30)
