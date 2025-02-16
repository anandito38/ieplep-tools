import streamlit as st

from io import BytesIO
from docx import Document
from fpdf import FPDF

from nbconvert import PDFExporter
import nbformat
from traitlets.config import Config
from nbconvert import HTMLExporter