import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.EAST
    assert state['row'] == 1
    assert state['col'] == 10


def test_south_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.SOUTH


def test_west_turn(robot):
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.WEST


def test_north_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.NORTH


def test_east_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST


def test_illegal_move_east(robot):


    with pytest.raises(IllegalMoveException):
        robot.move()

def test_illegal_south(robot):
    robot.turn()

    with pytest.raises(IllegalMoveException):
        robot.move()


def test_illegal_west(robot):
    robot._state.col = 1
    robot._state.direction = Direction.WEST
    with pytest.raises(IllegalMoveException):

        robot.move()


def test_illegal_north(robot):
    robot._state.row = 1
    robot._state.direction = Direction.NORTH
    with pytest.raises(IllegalMoveException):

        robot.move()

def test_move_north(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    robot.move()

    state = robot.state()
    assert state['row'] == 2
    assert state['col'] == 10





def test_move_south(robot):
    robot._state.direction = Direction.SOUTH
    robot._state.row = 1
    robot.move()



def test_move_west(robot):
    robot.turn()
    robot.turn()
    robot.move()

def test_move_east(robot):
    robot._state.col = 1
    robot.move()





def test_back_track_without_history(robot):
    with pytest.raises(IndexError):
        robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.EAST
    assert state['row'] == 1
    assert state['col'] == 10


def test_back_track_move(robot):
    robot._state.row = 2
    robot._state.direction = Direction.NORTH
    robot._state.col = 2
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 2
    assert state['col'] == 2


def test_back_track_turn(robot):
    robot.turn()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.EAST
    assert state['row'] == 1
    assert state['col'] == 10






def test_back_track_multimove_one(robot):
    robot._state.row = 2
    robot._state.direction = Direction.NORTH
    robot._state.col = 2
    robot.move()
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 3
    assert state['col'] == 2

def test_back_track_multimove_all(robot):
    robot._state.row = 2
    robot._state.direction = Direction.NORTH
    robot._state.col = 2
    robot.move()
    robot.move()
    robot.back_track()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 2
    assert state['col'] == 2