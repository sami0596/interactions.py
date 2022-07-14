from typing import overload, Type, TypeVar, List, Iterable, Optional, Callable, Awaitable, Literal, Coroutine, Union

from interactions.client.bot import Client
from enum import Enum
from ..api.models.channel import Channel
from ..api.models.guild import Guild
from ..api.models.member import Member
from ..api.models.message import Message, Emoji, Sticker
from ..api.models.user import User
from ..api.models.webhook import Webhook
from ..api.models.role import Role
from ..api.http.client import HTTPClient

_SA = TypeVar("_SA", Channel, Guild, Webhook, User, Sticker)
_MA = TypeVar("_MA", Member, Emoji, Role, Message)
_T = TypeVar("_T")

__all__: tuple

class Force(str, Enum):
    """
    An enum representing the force methods for the get method
    """
    CACHE: str
    HTTP: str

# not API-object related
@overload
def get(
    items: Iterable[_T], /, *, id: Optional[int] = None, name: Optional[str] = None, check: Callable[..., bool], **kwargs
) -> Optional[_T]: ...

# API-object related

# with http force
# single objects
@overload
def get(
    client: Client,
    obj: Type[_SA],
    *,
    object_id: int,
    force: Optional[Literal["http", Force.HTTP]] = None
) -> Awaitable[_SA]: ...

@overload
def get(
    client: Client,
    obj: Type[_MA],
    *,
    parent_id: int,
    object_id: int,
    force: Optional[Literal["http", Force.HTTP]] = None
) -> Awaitable[_MA]: ...

# list of objects
@overload
def get(
    client: Client,
    obj: Type[List[_SA]],
    *,
    object_ids: List[int],
    force: Optional[Literal["http", Force.HTTP]] = None
) -> Awaitable[List[_SA]]: ...

@overload
def get(
    client: Client,
    obj: Type[List[_MA]],
    *,
    parent_id: int,
    object_ids: List[int],
    force: Optional[Literal["http", Force.HTTP]] = None
) -> Awaitable[List[_MA]]: ...

# with cache force
@overload
def get(client: Client, obj: Type[_SA], *, object_id: int, force: Literal["cache", Force.CACHE]) -> Optional[_SA]: ...

@overload
def get(
    client: Client, obj: Type[_MA], *, parent_id: int, object_id: int, force: Literal["cache", Force.CACHE]
) -> Optional[_MA]: ...

# list of objects
@overload
def get(
    client: Client, obj: Type[List[_SA]], *, object_ids: List[int], force: Literal["cache", Force.CACHE]
) -> List[Optional[_SA]]: ...

@overload
def get(
    client: Client,
    obj: Type[List[_MA]],
    *,
    parent_id: int,
    object_ids: List[int],
    force: Literal["cache", Force.CACHE]
) -> List[Optional[_MA]]: ...

# Having a not-overloaded definition stops showing a warning/complaint from the IDE if wrong arguments are put in,
# so we'll leave that out

def _search_iterable(item: Iterable[_T], **kwargs) -> Optional[_T]:...
def _get_cache(
    _object: Type[_T], client: Client, kwarg_name: str, _list: bool = False, **kwargs
) -> Union[Optional[_T], List[Optional[_T]]]:...
async def _return_cache(
    obj: Union[Optional[_T], List[Optional[_T]]]
) -> Union[Optional[_T], List[Optional[_T]]]:...
async def _http_request(
    obj: Type[_T],
    http: HTTPClient,
    request: Union[Coroutine, List[Union[_T, Coroutine]], List[Coroutine]] = None,
    _name: str = None,
    **kwargs,
) -> Union[_T, List[_T]]:...