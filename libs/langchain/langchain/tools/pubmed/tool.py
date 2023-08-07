"""Tool for the Pubmed API."""

from typing import Optional

try:
    from pydantic.v1 import Field
except:
    from pydantic import Field

from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain.tools.base import BaseTool
from langchain.utilities.pupmed import PubMedAPIWrapper


class PubmedQueryRun(BaseTool):
    """Tool that searches the PubMed API."""

    name = "PubMed"
    description = (
        "A wrapper around PubMed.org "
        "Useful for when you need to answer questions about Physics, Mathematics, "
        "Computer Science, Quantitative Biology, Quantitative Finance, Statistics, "
        "Electrical Engineering, and Economics "
        "from scientific articles on PubMed.org. "
        "Input should be a search query."
    )
    api_wrapper: PubMedAPIWrapper = Field(default_factory=PubMedAPIWrapper)

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the Arxiv tool."""
        return self.api_wrapper.run(query)
