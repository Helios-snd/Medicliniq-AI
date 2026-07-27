from app.api.v1 import(
    health,
    auth,
    health_profile,
    medical_history,
    medications,
    allergies,
    doctor,
    lab_reports,
    symptom,
    vital,
)

v1_routes = [
    health.router,
    auth.router,
    health_profile.router,
    medical_history.router,
    medications.router,
    allergies.router,
    doctor.router,
    lab_reports.router,
    symptom.router,
    vital.router,
]

__all__ = ["v1_routes"]

