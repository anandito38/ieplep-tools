import streamlit as st

from io import BytesIO
from docx import Document
from fpdf import FPDF

from nbconvert import PDFExporter
from traitlets.config import Config
from nbconvert import HTMLExporter
from traitlets.config import Config
import nbformat
import subprocess
import os