import isodate
import datetime
from typing import Optional
from pydantic import BaseModel, validator

class CameraEvent(BaseModel):
    device: object
    start_time: datetime.datetime
    duration: datetime.timedelta

    end_time: Optional[datetime.datetime] = None

    @validator("end_time", pre=True, always=True)
    def set_end_time(cls, v, values, **kwargs):
        """Set the eggs field based upon a spam value."""
        return values.get('start_time')+ values.get('duration')
    
    @property
    def event_id(self):
        """Set the eggs field based upon a spam value."""
        return f"{self.start_time.isoformat()}->{self.end_time.isoformat()}|{self.device.device_id}"

    @classmethod
    def from_attrib(cls, xml_period_attributes : dict, nest_device):
        return CameraEvent(
            device=nest_device,
            start_time=datetime.datetime.fromisoformat(xml_period_attributes["programDateTime"]),
            duration=min(datetime.timedelta(minutes=1), isodate.parse_duration(xml_period_attributes["duration"]))
        )