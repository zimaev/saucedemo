from page_factory.component import Component


class ErrorMessage(Component):
    @property
    def type_of(self) -> str:
        return 'error message'
