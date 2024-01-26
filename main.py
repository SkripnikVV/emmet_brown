"""
main.py
-------
Testing task for Staffcop
Not based on: https://github.com/Boring-Mind/Ant-assignment )))
"""
import sys
import logging
from collections import deque

STEP = 1
LIMIT = 25

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
logger.info(sys.version_info)


class Emmet:
    def __init__(self, x=1000, y=1000, step=STEP, limit=LIMIT):
        """
        Initializing Dr. Brown
        Args:
            x (int): birth point along the x axis
            y (int): birth point along the y axis
            step (int): emmet movement step
            limit (int): intercept
        """
        self.process_log_limit = 1000
        self._count = 0
        self._completed_count = 0
        self._entry_point = (x, y)
        self._step = step
        self._limit = limit
        self._completed_points = set()
        self._visited_points = set()
        self._points_for_evaluation = deque()
        self._add_point_for_evaluation(self._entry_point)
        logger.info('the Emmet Brown was born at the point %s', self._entry_point)

    def run(self):
        """launching an emmet"""
        while True:
            if len(self._points_for_evaluation) == 0:
                break
            point = self._points_for_evaluation.pop()
            if self._point_is_available(*point):
                self._add_point_to_visited(point)
                self._get_next_points(*point)
            self._add_point_to_completed(point)
            self._process_log()

    @property
    def count(self):
        """
        Property returns the number of available points
        Returns:
            int: number of available points
        """
        return self._count

    def report(self):
        """
        The method logs the results of the work
        """
        logger.info('the Emmet Brown can visit %s points', self.count)

    def _process_log(self):
        """
        The method displays periodic messages about the work progress in the log.
        """
        if self._completed_count % self.process_log_limit == 0:
            logger.info('process... completed %s points, available %s points',
                        self._completed_count, self._count)

    def _add_point_for_evaluation(self, point):
        """
        The method adds a point to the queue for evaluation
        Args:
            point (tuple[int, int]): point on an endless board
        """
        self._points_for_evaluation.append(point)

    def _add_point_to_visited(self, point):
        """
        The method adds a point to the list that an Emmet can visit
        Args:
            point (tuple[int, int]): point on an endless board
        """
        if point not in self._visited_points:
            self._count += 1
            self._visited_points.add(point)

    def _point_is_available(self, x, y):
        """
        The method checks the accessibility of a point for an Emmet
        Args:
            x (int): x coordinate
            y (int): y coordinate

        Returns:
            True if the point is available, False otherwise
        """
        point = (x, y)
        if point in self._completed_points or point in self._visited_points:
            return
        if sum(map(int, list(str(abs(x)) + str(abs(y))))) <= self._limit:
            return True
        return False

    def _point_is_completed(self, point):
        """
        The method determines whether a given point has been processed or not
        Args:
            point (tuple[int, int]): point on an endless board

        Returns:
            True if the point is not completed, False otherwise
        """
        return point not in self._completed_points

    def _add_point_to_completed(self, point):
        """
        The method adds a point to the list of completed
        Args:
            point (tuple[int, int]): point on an endless board
        """
        if not point in self._completed_points:
            self._completed_points.add(point)
            self._completed_count += 1

    def _get_next_points(self, x, y):
        """
        The method adds new points to the check queue
        Args:
            x (int): x coordinate
            y (int): y coordinate
        """
        points = ((x - self._step, y), (x + self._step, y), (x, y - self._step), (x, y + self._step))
        [self._add_point_for_evaluation(point) for point in points if self._point_is_completed(point)]


def main():
    """main function"""
    emmet = Emmet(1000, 1000)
    emmet.run()
    emmet.report()


if __name__ == '__main__':
    main()
