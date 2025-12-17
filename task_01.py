import heapq


def min_value_of_cables_connection(cable_len):
    """
    Calculate cable1 minimum total cost to connect all cables.
    """

    if len(cable_len) <= 1:
        return 0

    heap = cable_len.copy()
    heapq.heapify(heap)
    total_cost = 0

    while len(heap) > 1:
        cable1 = heapq.heappop(heap)

        cable2 = heapq.heappop(heap)
        cost = cable1 + cable2
        total_cost += cost
        heapq.heappush(heap, cost)

    return total_cost


if __name__ == "__main__":
    lengths = [8, 4, 6, 12]

    result = min_value_of_cables_connection(lengths)
    print("Minimum cost of cables connection:", result)
