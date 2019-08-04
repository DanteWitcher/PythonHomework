from ..enums.types import Types


operators = (
    {
        'type': Types.EVAL,
        'value': '^',
        'right_value': '**'
    },
    {
        'type': Types.EXEC,
        'value': 'log',
        'right_value': 'log'
    },
    # TO DO: work around
    {
        'type': Types.ERROR,
        'value': 'abs',
        'right_value': 'abs'
    },
    {
        'type': Types.EXEC,
        'value': 'abs(',
        'right_value': 'abs('
    },
)
