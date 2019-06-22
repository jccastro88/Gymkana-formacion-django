from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.file.size
    limit_max = 10*1024*1024
    # 10 MB = 10485760 Bytes
    if filesize > limit_max:
        raise ValidationError("El tamaño máximo del archivo no puede ser superior a 10MB")
    else:
        return value
