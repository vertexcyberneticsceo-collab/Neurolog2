from math import sqrt
from statistics import mean, pstdev

from schemas import SensorSample


def vector_magnitude(x: float, y: float, z: float) -> float:
    return sqrt((x * x) + (y * y) + (z * z))


def detect_possible_event(
    samples: list[SensorSample],
) -> tuple[bool, float, str]:
    if len(samples) < 10:
        return False, 0.0, "Not enough samples."

    non_walking_ratio = (
        sum(not sample.walking_detected for sample in samples)
        / len(samples)
    )

    if non_walking_ratio < 0.7:
        return False, 0.0, "Movement resembles walking."

    accel_values = [
        vector_magnitude(
            sample.accel_x,
            sample.accel_y,
            sample.accel_z,
        )
        for sample in samples
    ]

    gyro_values = [
        vector_magnitude(
            sample.gyro_x,
            sample.gyro_y,
            sample.gyro_z,
        )
        for sample in samples
    ]

    motion_score = min(
        (
            mean(accel_values)
            + pstdev(accel_values)
            + mean(gyro_values)
        ) / 12,
        1,
    )

    heart_rates = [
        sample.heart_rate
        for sample in samples
        if sample.heart_rate is not None
    ]

    heart_rate_score = (
        min(max((mean(heart_rates) - 90) / 50, 0), 1)
        if heart_rates
        else 0
    )

    stress_levels = [
        sample.stress_level
        for sample in samples
        if sample.stress_level is not None
    ]

    stress_score = (
        min(max((mean(stress_levels) - 50) / 50, 0), 1)
        if stress_levels
        else 0
    )

    confidence = round(
        (motion_score * 0.7)
        + (heart_rate_score * 0.2)
        + (stress_score * 0.1),
        3,
    )

    if confidence >= 0.65:
        return (
            True,
            confidence,
            "High non-walking motion detected.",
        )

    return False, confidence, "Signal below threshold."
