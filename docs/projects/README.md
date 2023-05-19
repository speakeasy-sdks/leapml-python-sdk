# projects

### Available Operations

* [projects_controller_remove](#projects_controller_remove) - Delete a Project

## projects_controller_remove

Delete a Project

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()

req = operations.ProjectsControllerRemoveRequest(
    project_id='sapiente',
)

res = s.projects.projects_controller_remove(req, operations.ProjectsControllerRemoveSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```
