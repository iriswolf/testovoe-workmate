from app.infrastructure.exceptions.base import InfrastructureError


class DescriptorError(InfrastructureError): ...


class CSVDialectValidationError(DescriptorError): ...


class EncodingValidationError(DescriptorError): ...
