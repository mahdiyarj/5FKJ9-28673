import sys

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Reservation, Restaurant, Table
from .serializers import ReservationSerializer


@api_view(["POST"])
def book(request):
    number_of_individuals = request.data.get("number_of_individuals")
    number_of_individuals = int(number_of_individuals)

    if number_of_individuals % 2 != 0:
        number_of_individuals += 1

    available_tables = Table.objects.filter(
        booking__isnull=True, capacity__gte=number_of_individuals
    )
    seat_price = Restaurant.objects.first().seat_price
    cost = sys.maxsize
    selected_table = None

    for table in available_tables:
        cost_1 = seat_price * number_of_individuals
        cost_2 = (table.capacity - 1) * seat_price
        min_cost = min(cost_1, cost_2)

        if cost > min_cost:
            cost = min_cost
            selected_table = table.table_id

    if not selected_table:
        return Response({"message": "No tables available"})

    reservation = Reservation()
    reservation.table = selected_table
    reservation.user_id = 1
    reservation.cost = cost
    reservation.number_of_seats = number_of_individuals
    reservation.save()

    reservation_serializer = ReservationSerializer(reservation)

    return Response(reservation_serializer.data)
