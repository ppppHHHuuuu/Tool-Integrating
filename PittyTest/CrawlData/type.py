from dataclasses import dataclass
from enum import Enum

@dataclass
class AnalysisIssue:
    contract: str #slither
    source_map: str #slither
    line_no: str #slither
    code: str #??
    description: str #slither
    hint: str
    issue_title: str
    swcID: str
    swc_title: str
    swc_link: str
    severity: str

