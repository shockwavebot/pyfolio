


## Threading Decision Matrix

| Need | Use This |
|------|----------|
| Protect shared data from concurrent modification | **Lock/RLock** |
| Signal completion or state change | **Event** |
| Limit concurrent access to resource | **Semaphore** |
| Complex condition-based waiting | **Condition** |
| Synchronize multiple threads at checkpoint | **Barrier** |
| Execute something after delay | **Timer** |
| Same thread needs lock multiple times | **RLock** |
| Prevent resource pool overflow | **BoundedSemaphore** |

