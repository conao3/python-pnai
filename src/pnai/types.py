import subprocess

import pydantic


class Result(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(arbitrary_types_allowed=True)

    proc: subprocess.CompletedProcess[bytes]
