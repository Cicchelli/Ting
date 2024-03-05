from ting_file_management.priority_queue import PriorityQueue


import pytest


def test_basic_priority_queueing():
    """
    Testa as funcionalidades básicas de uma fila de prioridade.

    """
    # Arrange
    priority_queue = PriorityQueue()

    # Assert
    assert len(priority_queue) == 0
    assert len(priority_queue.high_priority) == 0
    assert len(priority_queue.regular_priority) == 0

    # Act
    for i in range(1, 5):
        priority_queue.enqueue({"qtd_linhas": i * 2})

    # Assert
    assert len(priority_queue) == 4
    assert len(priority_queue.high_priority) == 2
    assert len(priority_queue.regular_priority) == 2

    # Act
    priority_queue.dequeue()

    # Assert
    assert len(priority_queue) == 3
    assert len(priority_queue.high_priority) == 1
    assert len(priority_queue.regular_priority) == 2

    # Act & Assert
    file = priority_queue.search(0)
    assert file["qtd_linhas"] == 4

    # Assert
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(420)
