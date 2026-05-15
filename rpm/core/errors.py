from http import HTTPStatus

from fastapi import HTTPException


class ApiException(HTTPException):
    def __init__(self, status_code: int, detail: str, error_code: str):
        super().__init__(
            status_code=status_code,
            detail=detail,
            headers={'X-Error-Code': error_code},
        )


class NotFoundException(ApiException):
    def __init__(self, entity, entity_id):
        entity_name = entity.__name__
        super().__init__(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'{entity_name} with id {entity_id} not found',
            error_code='NOT_FOUND',
        )


class ConflictException(ApiException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=HTTPStatus.CONFLICT,
            detail=detail,
            error_code='RESOURCE_ALREADY_EXISTS',
        )


class BadRequestException(ApiException):
    def __init__(self, detail: str, error_code: str = 'BAD_REQUEST'):
        super().__init__(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=detail,
            error_code=error_code,
        )


class UnauthorizedException(ApiException):
    def __init__(self, detail: str = 'Não autorizado'):
        super().__init__(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail=detail,
            error_code='UNAUTHORIZED',
        )
