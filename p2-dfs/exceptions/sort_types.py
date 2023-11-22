class BadSortTypeArgument(Exception):
    def __init__(self) -> None:
        valid_sort_type = ['dfs', 'bfs']
        message = 'Must be one of these: ' + ', '.join(valid_sort_type)
        super().__init__(message)