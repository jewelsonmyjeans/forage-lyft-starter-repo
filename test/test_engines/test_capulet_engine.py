import unittest

from engines.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self) -> None:
        """
        Test engine should be serviced when current mileage exceeds service limit threshold.

        Parameters:
        - self: The test case instance.

        Returns:
        - None
        """
        current_mileage: int = 30001
        last_service_mileage: int = 0
        engine: CapuletEngine = CapuletEngine(
            current_mileage, last_service_mileage
        )

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self) -> None:
        """
        Test engine should not be serviced when current mileage is below service limit threshold.

        :param self: The test case instance.
        :return: None
        """
        current_mileage: int = 30000
        last_service_mileage: int = 0
        engine: CapuletEngine = CapuletEngine(
            current_mileage, last_service_mileage
        )

        self.assertFalse(engine.needs_service())


if __name__ == "main":
    unittest.main()