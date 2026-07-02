from pydantic import BaseModel

class MachineInput(BaseModel):
    Type: str
    Air_temperature_K: float
    Process_temperature_K: float
    Rotational_speed_rpm: int
    Torque_Nm: float
    Tool_wear_min: int
    #Temp_Diff: float
    #Power: float


class ChatRequest(BaseModel):
    question: str

