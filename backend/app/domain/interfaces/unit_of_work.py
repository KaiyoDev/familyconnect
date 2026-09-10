"""Transaction boundary used by application services."""
from abc import ABC, abstractmethod


class IUnitOfWork(ABC):
    """Abstract transaction boundary; infrastructure supplies the adapter."""

    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def rollback(self) -> None: ...
