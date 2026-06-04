d
\begin{filecontents*}[overwrite]{references.bib}
@inproceedings{leis2014morsel,
  author    = {Viktor Leis and Peter Boncz and Alfons Kemper and Thomas Neumann},
  title     = {Morsel-Driven Parallelism: A {NUMA}-Aware Query Evaluation Framework for the Many-Core Age},
  booktitle = {Proceedings of the 2014 ACM SIGMOD International Conference on Management of Data},
  pages     = {743--754},
  year      = {2014},
  publisher = {ACM},
  doi       = {10.1145/2588555.2610507},
  url       = {https://db.in.tum.de/~leis/papers/morsels.pdf}
}
@article{graefe1994volcano,
  author  = {Goetz Graefe},
  title   = {Volcano---An Extensible and Parallel Query Evaluation System},
  journal = {IEEE Transactions on Knowledge and Data Engineering},
  volume  = {6},
  number  = {1},
  pages   = {120--135},
  year    = {1994},
  doi     = {10.1109/69.273032}
}
@article{neumann2011compiling,
  author  = {Thomas Neumann},
  title   = {Efficiently Compiling Efficient Query Plans for Modern Hardware},
  journal = {Proceedings of the VLDB Endowment},
  volume  = {4},
  number  = {9},
  pages   = {539--550},
  year    = {2011},
  url     = {http://www.vldb.org/pvldb/vol4/p539-neumann.pdf}
}
@inproceedings{boncz2005x100,
  author    = {Peter A. Boncz and Marcin Zukowski and Niels Nes},
  title     = {{MonetDB}/X100: Hyper-Pipelining Query Execution},
  booktitle = {CIDR},
  pages     = {225--237},
  year      = {2005},
  url       = {https://www.cidrdb.org/cidr2005/papers/P19.pdf}
}
@article{melnik2010dremel,
  author  = {Sergey Melnik and Andrey Gubarev and Jing Jing Long and Geoffrey Romer and Shiva Shivakumar and Matt Tolton and Theo Vassilakis},
  title   = {Dremel: Interactive Analysis of Web-Scale Datasets},
  journal = {Proceedings of the VLDB Endowment},
  volume  = {3},
  number  = {1},
  pages   = {330--339},
  year    = {2010}
}
@inproceedings{moritz2018ray,
  author    = {Philipp Moritz and Robert Nishihara and Stephanie Wang and Alexey Tumanov and Richard Liaw and Eric Liang and Melih Elibol and Zongheng Yang and William Paul and Michael I. Jordan and Ion Stoica},
  title     = {Ray: A Distributed Framework for Emerging {AI} Applications},
  booktitle = {13th USENIX Symposium on Operating Systems Design and Implementation (OSDI 18)},
  pages     = {561--577},
  year      = {2018},
  url       = {https://www.usenix.org/system/files/osdi18-moritz.pdf}
}
@misc{daftarch,
  author = {{Eventual}},
  title  = {Daft Architecture},
  year   = {2025},
  url    = {https://docs.daft.ai/en/stable/architecture/}
}
@misc{daftflotilla,
  author = {Colin Ho},
  title  = {Introducing Flotilla: Simplifying Multimodal Data Processing at Scale},
  year   = {2025},
  month  = oct,
  url    = {https://www.daft.ai/blog/introducing-flotilla-simplifying-multimodal-data-processing-at-scale}
}
@misc{daftswordfish,
  author = {Colin Ho and {ByteDance Volcano Engine}},
  title  = {Exploring Daft's Local Execution: The Swordfish Engine},
  year   = {2025},
  month  = sep,
  url    = {https://www.daft.ai/blog/exploring-daft-swordfish-execution-mechanism}
}
@misc{daftbench,
  author = {Colin Ho},
  title  = {Benchmarks for Multimodal AI: Spark, Ray Data, and Daft},
  year   = {2025},
  url    = {https://www.daft.ai/blog/benchmarks-for-multimodal-ai-workloads}
}
@misc{daftv076,
  author = {{Daft Team}},
  title  = {Daft v0.7.6: Every Major Lake Format, O(1) Scalars, and Swordfish Plan Caching},
  year   = {2025},
  url    = {https://www.daft.ai/blog/daft-v076-o1-scalars-kafka-reads-and-a-full-observability-pipeline}
}
@misc{daftrepo,
  author = {{Eventual-Inc}},
  title  = {Daft GitHub Repository},
  year   = {2025},
  url    = {https://github.com/Eventual-Inc/Daft}
}
@misc{whyduckdb,
  author = {{DuckDB Labs}},
  title  = {Why DuckDB},
  year   = {2025},
  url    = {https://duckdb.org/why_duckdb}
}
@misc{duckdbpush,
  author = {Mark Raasveldt},
  title  = {Push-Based Execution in {DuckDB}},
  year   = {2021},
  month  = nov,
  url    = {https://dsdsd.da.cwi.nl/past_talks/duckdb-push-based-execution/}
}
@misc{duckdbpr2393,
  author = {Mark Raasveldt},
  title  = {Switch to Push-Based Execution Model (PR \#2393)},
  year   = {2021},
  url    = {https://github.com/duckdb/duckdb/pull/2393}
}
@misc{arrowcolumnar,
  author = {{Apache Arrow}},
  title  = {Arrow Columnar Format Specification},
  year   = {2025},
  url    = {https://arrow.apache.org/docs/format/Columnar.html}
}
@misc{parquetformat,
  author = {{Apache Parquet}},
  title  = {Parquet Format Specification},
  year   = {2025},
  url    = {https://github.com/apache/parquet-format}
}
@misc{parquetconfig,
  author = {{Apache Parquet}},
  title  = {Configurations},
  year   = {2025},
  url    = {https://parquet.apache.org/docs/file-format/configurations/}
}
@misc{pyarrowparquet,
  author = {{Apache Arrow}},
  title  = {Reading and Writing the Apache Parquet Format (PyArrow)},
  year   = {2025},
  url    = {https://arrow.apache.org/docs/python/parquet.html}
}
@misc{polars1,
  author = {Ritchie Vink},
  title  = {Announcing Polars 1.0},
  year   = {2024},
  month  = jul,
  url    = {https://pola.rs/posts/announcing-polars-1/}
}
@misc{polarsstream,
  author = {{Polars}},
  title  = {Polars in Aggregate: Polars Cloud, Streaming engine, and New Data Types},
  year   = {2025},
  url    = {https://pola.rs/posts/polars-in-aggregate-dec25/}
}
@misc{laionaesthetics,
  author = {{LAION}},
  title  = {{LAION}-Aesthetics},
  year   = {2022},
  url    = {https://laion.ai/blog/laion-aesthetics/}
}
@misc{pythondataclasses,
  author = {{Python Software Foundation}},
  title  = {dataclasses --- Data Classes},
  year   = {2025},
  url    = {https://docs.python.org/3/library/dataclasses.html}
}
@misc{pythonasyncio,
  author = {{Python Software Foundation}},
  title  = {asyncio --- Asynchronous I/O},
  year   = {2025},
  url    = {https://docs.python.org/3/library/asyncio.html}
}
\end{filecontents*}

\usepackage[backend=biber,style=numeric,sorting=none]{biblatex}
\addbibresource{references.bib}

\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amsthm,amssymb}
\usepackage{xcolor}
\usepackage[colorlinks=true,linkcolor=blue!60!black,urlcolor=teal!70!black,citecolor=purple!60!black]{hyperref}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{fancyhdr}
\usepackage{listings}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,fit,calc,shapes.geometric}

% --- listings style for Python skeletons ---
\definecolor{kw}{RGB}{0,80,160}
\definecolor{str}{RGB}{160,40,40}
\definecolor{com}{RGB}{80,120,80}
\definecolor{bg}{RGB}{248,248,245}
\lstdefinestyle{py}{
  language=Python,
  basicstyle=\ttfamily\small,
  keywordstyle=\color{kw}\bfseries,
  stringstyle=\color{str},
  commentstyle=\color{com}\itshape,
  backgroundcolor=\color{bg},
  showstringspaces=false,
  breaklines=true,
  frame=single,
  rulecolor=\color{black!20},
  numbers=left,
  numberstyle=\tiny\color{black!50},
  framesep=4pt,
  xleftmargin=10pt
}
\lstset{style=py}

% --- theorem environments ---
\newtheoremstyle{def}{6pt}{6pt}{}{}{\bfseries\color{blue!50!black}}{.}{.5em}{}
\theoremstyle{def}
\newtheorem{Definition}{Definition}[chapter]
\newtheorem{Insight}{Insight}[chapter]
\newtheorem{Analogy}{Analogy}[chapter]
\newtheorem{Question}{Question}[chapter]
\newtheorem{ComprehensionCheck}{Comprehension Check}[chapter]
\newtheorem{Hint}{Hint}[chapter]

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\nouppercase{\leftmark}}
\fancyhead[LO]{\nouppercase{\rightmark}}

\title{\Huge\textbf{Mini-Daft: A Socratic Build Guide}\\[1ex]\Large Day-by-Day Implementation Companion for the Eventual On-Site}
\author{For a recent math grad with applied-ML experience,\\ preparing for the Eventual systems/data-infra interview.}
\date{}

\begin{document}
\frontmatter
\maketitle
\tableofcontents

\chapter*{Preface: How to Use This Guide}
\addcontentsline{toc}{chapter}{Preface}

This guide is a \emph{Socratic build companion} for ten days of building \texttt{minidaft}, a small multimodal data engine in pure Python. It is not a textbook. It does not replace your existing textbook chapters; it sits beside them. The textbook tells you \emph{what} a morsel-driven engine is; this guide asks you the questions and gives you the file scaffolding so that by Day 10 you have \emph{built} one.

\textbf{The rhythm of each day.} Read the orientation (5 min). Open the textbook chapter the day points to. Sit with the leading questions for ten minutes before reading on. Build, using only signatures and hints from the build plan --- no implementation code is given to you here, on purpose. Run the tests. Answer the comprehension checks in your own words. Write the reflection paragraph before closing your laptop.

\textbf{The no-code-blocks rule.} You will not find a single working function body in this book. You will find class skeletons (fields and types), method signatures with docstring placeholders, and named API hints (``you'll want \texttt{pyarrow.parquet.ParquetFile.metadata}''). Implementations are yours. That is not a stylistic choice; it is the entire pedagogy. If you copy code from this book, you have learned nothing; if you write the code yourself from the signatures, you have learned everything.

\textbf{Why this matters for the on-site.} Eventual builds Daft, a high-performance multimodal data engine \cite{daftarch,daftrepo}. Jay pointed you at \emph{Why DuckDB} \cite{whyduckdb} and the Leis et al.~morsel-driven paper \cite{leis2014morsel} for a reason: Daft's native runner (Swordfish) is a streaming, push-based, morsel-driven engine in Rust \cite{daftswordfish}. You are not going to out-Rust the Eventual team in ten days. You \emph{can}, in ten days, hold the same mental model they hold. That is what gets you the offer.

\mainmatter

% =====================================================================
\chapter{Appendix A: The Python You Actually Need}
\label{ch:appA}

This appendix sits at the front of the book because every day refers back to it. Read each section once now, then return whenever a Day chapter sends you here.

\section{Dataclasses}
A dataclass is a regular class where Python writes \texttt{\_\_init\_\_}, \texttt{\_\_repr\_\_}, and \texttt{\_\_eq\_\_} for you, given the field declarations \cite{pythondataclasses}.

\begin{lstlisting}
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass(frozen=True)
class LogicalPlan:
    """Base class for all logical plan nodes. Frozen = immutable."""
    children: List["LogicalPlan"] = field(default_factory=list)
\end{lstlisting}

\begin{Question}
Why \texttt{field(default\_factory=list)} instead of \texttt{= []}? Predict what would happen if two \texttt{LogicalPlan} instances were constructed with the default and one mutated its children list.
\end{Question}

\begin{Insight}
Required fields (no default) must be declared \emph{before} fields with defaults. Mixing the order will raise at class-creation time, not at instance-creation time. This will bite you on Day 4.
\end{Insight}

\begin{ComprehensionCheck}
A subclass of a frozen dataclass that itself forgets the \texttt{@dataclass} decorator will silently lose any new fields from \texttt{\_\_init\_\_}. Why?
\end{ComprehensionCheck}

\section{References vs.~Values}
\texttt{x = y} does not copy. \texttt{is} compares identity, \texttt{==} compares value. Mutable defaults are aliased across calls. These three sentences explain at least 30\% of the bugs you will write this week.

\begin{Hint}
If two tests pass in isolation but fail when run together, suspect an aliased mutable default.
\end{Hint}

\section{Imports, \texttt{\_\_init\_\_.py}, \texttt{conftest.py}}
A folder becomes a package when it contains \texttt{\_\_init\_\_.py}. \texttt{python script.py} and \texttt{pytest} compute \texttt{sys.path} differently. Drop an empty \texttt{conftest.py} at your project root so pytest treats it as the import root.

\section{Pytest in 90 Seconds}
A test is a function named \texttt{test\_*} in a file named \texttt{test\_*.py}. Use plain \texttt{assert}. Fixtures are functions decorated with \texttt{@pytest.fixture}; receive them by naming a parameter the same as the fixture. Run from the project root.

\section{Type Hints You Will Use}
Use \texttt{List["LogicalPlan"]} (forward reference as string) when the class refers to itself. \texttt{Optional[X]} means ``X or None''. \texttt{Tuple[int, int]} is a fixed-size pair. \texttt{Callable[[int], str]} is ``a function from int to str''.

\section{Decorators in One Paragraph}
A decorator is a function that takes a function and returns a function. \texttt{@dataclass} on a class is the same as \texttt{MyClass = dataclass(MyClass)}. That is the entire mystery.

\section{asyncio for Days 8--9}
\texttt{async def f()} returns a coroutine, not a value. You must \texttt{await} it (or pass it to \texttt{asyncio.run} or \texttt{asyncio.gather}) for it to run \cite{pythonasyncio}. \texttt{asyncio.Queue(maxsize=N)} blocks the producer when full --- that is your backpressure mechanism. \texttt{asyncio.Semaphore(k)} caps concurrency at $k$. \texttt{asyncio.gather(*coros)} runs them concurrently and waits for all.

\begin{Question}
Why does a bounded \texttt{asyncio.Queue} give you backpressure for free, while an unbounded one would not?
\end{Question}

\section{The GIL, in One Paragraph}
CPython holds a global lock that allows only one thread to execute Python bytecode at a time. asyncio gets concurrency, not parallelism, in pure Python. For Day 8, that means our ``work-stealing'' demonstrates the \emph{control structure} of work-stealing; the wall-clock speedup will come from the CPU operators being implemented in C extensions (pyarrow). Be honest about this in your reflection.

\section{pyarrow Conceptual Map}
A \texttt{pa.Array} is a typed column. A \texttt{pa.RecordBatch} is a list of arrays sharing a schema. A \texttt{pa.Table} is a vertical stack of RecordBatches. A \texttt{pa.Schema} is the list of (name, type) pairs. Arrays in memory follow the Arrow Columnar Format spec, which recommends 64-byte alignment so loops can use SIMD/AVX-512 registers without conditional checks \cite{arrowcolumnar}.

% =====================================================================
\chapter{Day 0 --- Environment Setup}

\section*{Orientation (5 min read)}
You will produce a clean, importable \texttt{minidaft} package, a venv, a \texttt{requirements.txt}, and a passing pytest collection (even with zero tests). Total work: about 4 hours. Light day on purpose --- Day 1 was already a marathon.

\section*{Read first}
Skim Chapter 1 of your textbook (the engine landscape). Skim DuckDB's ``Why DuckDB'' page \cite{whyduckdb} to internalize what an embedded, in-process analytics engine even is.

\section*{Intuition}
\begin{Analogy}
A Python package is a \emph{house}; a module is a \emph{room}; \texttt{\_\_init\_\_.py} is the front door that tells visitors the rooms exist.
\end{Analogy}

\section*{Leading Questions}
\begin{enumerate}
  \item Why is naming a module \texttt{types.py} a footgun?
  \item What is the difference between \texttt{python -m pytest} and \texttt{pytest}?
  \item Why does a \texttt{.gitignore} file have a leading dot and \emph{no} \texttt{.txt} extension?
\end{enumerate}

\section*{Build Plan}
Create the layout: \texttt{minidaft/} (the package, with \texttt{\_\_init\_\_.py}, plus subfolders \texttt{io/}, \texttt{ops/}, \texttt{exec/}, \texttt{dtypes.py}), \texttt{tests/}, \texttt{conftest.py} (empty, at project root), \texttt{requirements.txt} (\texttt{pyarrow}, \texttt{pytest}, \texttt{pillow}, \texttt{requests}, \texttt{numpy}, \texttt{psutil}, \texttt{matplotlib}). Add a \texttt{.gitignore} that excludes \texttt{.venv/}, \texttt{\_\_pycache\_\_/}, \texttt{*.egg-info/}.

\section*{Tests to write}
A single \texttt{tests/test\_smoke.py} with one assertion: ``import \texttt{minidaft}; assert it has \texttt{\_\_version\_\_}.''

\section*{Comprehension Checks}
(1) Why does Daft expose its package as \texttt{daft} but the GitHub repo as \texttt{Daft}? (Hint: look at \texttt{Eventual-Inc/Daft} \cite{daftrepo}.) (2) Why is \texttt{dtypes.py} a safer file name than \texttt{types.py}?

\section*{Pitfalls}
File is \texttt{.gitignore} (no \texttt{.txt}). Do not name a module \texttt{types.py}. Make sure \texttt{conftest.py} is at the \emph{project root}, not inside \texttt{minidaft/}.

\section*{Definition of Done}
$\square$ \texttt{pytest} runs and collects 1 test. $\square$ \texttt{python -c "import minidaft; print(minidaft.\_\_version\_\_)"} prints. $\square$ Committed with message \texttt{Day 0: scaffold}.

\section*{Reflection}
What is the smallest unit of code that you can now ship reproducibly? Write three sentences.

% =====================================================================
\chapter{Day 1 --- Expression IR and Logical Plans (Recap)}

You already built this. Two pages, for reference.

\textbf{What you have.} \texttt{expressions.py} containing \texttt{Expr} as a base dataclass with subclasses \texttt{Col(name: str)}, \texttt{Lit(value)}, \texttt{BinOp(op, left, right)}, \texttt{FnCall(name, args, is\_expensive=False)}. \texttt{plan.py} containing \texttt{LogicalPlan} with subclasses \texttt{Source(path, schema)}, \texttt{Project(child, projections)}, \texttt{Filter(child, predicate)}, \texttt{Limit(child, n)}. An \texttt{.explain()} method on each that pretty-prints the tree.

\textbf{Where this lives in Daft.} Daft represents user code as a \texttt{LogicalPlan}, ``a tree of operators that describe what work should happen. Example operators include \texttt{Source}, \texttt{Project}, \texttt{Filter}, \texttt{GroupBy}, and \texttt{Join}'' \cite{daftarch}. Inside operators (especially \texttt{Project}) live expression trees of column references, literals, function calls, and UDFs --- exactly your \texttt{Expr} hierarchy.

\begin{Insight}
You have built two nested trees: a plan tree whose nodes contain expression trees. Hold this picture for the rest of the week.
\end{Insight}

\begin{ComprehensionCheck}
When the user writes \texttt{df.where(col("x") > 3).select(col("y"))}, draw the plan tree and the expression trees \emph{inside} the \texttt{Filter} and \texttt{Project} nodes.
\end{ComprehensionCheck}

\textbf{Reflection.} You can now describe \emph{what} a query is without saying anything about \emph{how} to run it. That separation is the whole game.

% =====================================================================
\chapter{Day 2 --- Arrow Types and Schema}

\section*{Orientation}
By end of day, \texttt{minidaft} has a \texttt{LogicalType} enum, a \texttt{Series} wrapper around \texttt{pa.Array}, a \texttt{Schema} dataclass, and a passing pandas-Arrow roundtrip test.

\section*{Read first}
Read \S2 of the textbook (columnar storage and Apache Arrow) before starting.

\section*{Intuition}
\begin{Analogy}
Columnar storage is a spreadsheet stored \emph{column-by-column} on disk. If you only need the sum of one column, you don't have to skim every row --- you read one contiguous stripe.
\end{Analogy}

\begin{Insight}
Arrow's columnar format recommends 64-byte alignment so that ``we can load the entire 64-byte buffer into a 512-bit wide SIMD register and get data-level parallelism on all the columnar values packed into the 64-byte buffer'' \cite{arrowcolumnar}.
\end{Insight}

\begin{figure}[h]
\centering
\begin{tikzpicture}[scale=0.7,every node/.style={font=\small}]
\node at (-2.5,2.2) {\textbf{Row layout}};
\foreach \r/\y in {0/1.6,1/1.1,2/0.6,3/0.1} {
  \foreach \c in {0,1,2} {
    \draw[fill=blue!10] (\c*1.0,\y) rectangle ++(0.9,0.4);
  }
}
\node at (5.5,2.2) {\textbf{Column layout}};
\foreach \c/\x in {0/5,1/6.1,2/7.2} {
  \foreach \r in {0,1,2,3} {
    \draw[fill=green!10] (\x,1.6-\r*0.4) rectangle ++(1.0,0.35);
  }
}
\draw[->,thick] (3.7,1.0) -- (4.7,1.0) node[midway,above]{transpose};
\end{tikzpicture}
\caption{Row vs.~column layout. The same 12 cells, very different I/O patterns.}
\end{figure}

\section*{Leading Questions}
\begin{enumerate}
  \item If a Parquet file stores 1M rows with 6 columns and you query just one column, reason from the physical layout: how much data do you have to read?
  \item Why does the Arrow spec specifically call out \emph{64} bytes? What CPU feature does that match?
  \item How do you find string \#500 in a variable-length string column without walking strings 1..499?
\end{enumerate}

\section*{Build Plan}
\textbf{File: \texttt{minidaft/dtypes.py}.}
\begin{lstlisting}
from enum import Enum

class LogicalType(Enum):
    """Daft-style logical types. NOT in types.py (stdlib collision)."""
    INT64 = "int64"
    FLOAT64 = "float64"
    STRING = "string"
    BOOL = "bool"
    BINARY = "binary"
    # multimodal types added on Day 6:
    # IMAGE_BYTES, IMAGE_DECODED, TENSOR
\end{lstlisting}

\textbf{File: \texttt{minidaft/series.py}.}
\begin{lstlisting}
from dataclasses import dataclass
import pyarrow as pa
from minidaft.dtypes import LogicalType

@dataclass
class Series:
    """Thin wrapper around pa.Array, tagged with a LogicalType."""
    name: str
    dtype: LogicalType
    array: pa.Array

    def __len__(self) -> int:
        """Return number of elements."""
        ...
\end{lstlisting}

\textbf{File: \texttt{minidaft/schema.py}.}
\begin{lstlisting}
from dataclasses import dataclass
from typing import List, Tuple
from minidaft.dtypes import LogicalType

@dataclass(frozen=True)
class Schema:
    """Ordered list of (name, dtype) pairs."""
    fields: Tuple[Tuple[str, LogicalType], ...]
\end{lstlisting}

\begin{Hint}
APIs you will reach for: \texttt{pyarrow.array(py\_list, type=...)}, \texttt{pyarrow.RecordBatch.from\_arrays(arrays, names=...)}, \texttt{pyarrow.schema([(name, type), ...])}, \texttt{pa.int64()}, \texttt{pa.string()}, \texttt{pa.list\_(pa.int8())}. Do not memorize; look them up at \cite{pyarrowparquet}.
\end{Hint}

\section*{Tests}
File: \texttt{tests/test\_day2.py}. (i) Roundtrip a 3-column pandas DataFrame through \texttt{Series} and back; assert frame-equality. (ii) Construct a Series with a wrong-typed array and assert it raises. (iii) Assert that \texttt{Schema} equality is value-equality, not identity.

\section*{Comprehension Checks}
\begin{enumerate}
  \item In your own words: why does columnar layout make \texttt{SUM(price)} fast but a row-by-row print slow?
  \item Why is a \texttt{LogicalType} enum useful even though pyarrow already has \texttt{pa.DataType}? (Hint: Day 6.)
\end{enumerate}

\section*{Pitfalls}
\texttt{dtypes.py} not \texttt{types.py}. \texttt{@dataclass(frozen=True)} requires you to use \texttt{object.\_\_setattr\_\_} if you ever need to mutate (don't). \texttt{Tuple[...,...]} is immutable; \texttt{List[...]} is not --- the schema uses tuples to remain hashable.

\section*{Definition of Done}
$\square$ 3 passing tests. $\square$ \texttt{Series} and \texttt{Schema} importable from the package. $\square$ Committed.

\section*{Reflection}
Explain in one paragraph: what does it mean to say Daft is ``built on Arrow''? Avoid jargon.

% =====================================================================
\chapter{Day 3 --- Parquet Scan with Pushdown}

\section*{Orientation}
End of day: \texttt{ParquetScan} reads a 10-row-group fixture and \emph{skips} row groups whose min/max excludes a predicate. You will observe by counting decoded row groups.

\section*{Read first}
\S3 of the textbook (Parquet file structure).

\section*{Intuition}
\begin{Analogy}
Parquet is a book with a table of contents that lists, per chapter, not only the chapter title but the min and max value of each chapter. If your question is ``find all chapters with chapter-number $> 200$'' and a chapter's recorded max is 150, you skip it without opening it.
\end{Analogy}

\begin{Definition}[Parquet hierarchy]
A Parquet \emph{file} contains one or more \emph{row groups}; each row group contains one \emph{column chunk} per column; each column chunk is split into \emph{pages}, the smallest decoded unit \cite{parquetformat}. The Parquet docs state: ``We recommend large row groups (512MB - 1GB). Since an entire row group might need to be read, we want it to completely fit on one HDFS block'' \cite{parquetconfig}.
\end{Definition}

\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=0.5cm,every node/.style={font=\small,draw,rounded corners,inner sep=4pt}]
\node (f) {Parquet File};
\node[below=of f] (rg1) {RowGroup 0};
\node[right=of rg1] (rg2) {RowGroup 1};
\node[right=of rg2] (rg3) {\dots};
\node[below=of rg1] (cc) {ColChunk (price)};
\node[below=of cc] (p1) {Page 0};
\node[right=of p1] (p2) {Page 1};
\draw[->] (f) -- (rg1); \draw[->] (f) -- (rg2); \draw[->] (f) -- (rg3);
\draw[->] (rg1) -- (cc); \draw[->] (cc) -- (p1); \draw[->] (cc) -- (p2);
\end{tikzpicture}
\caption{Parquet file $\to$ row groups $\to$ column chunks $\to$ pages. Statistics (min/max/null-count) live at the column-chunk level.}
\end{figure}

\section*{Leading Questions}
\begin{enumerate}
  \item Where exactly are min/max statistics stored in a Parquet file? At what granularity?
  \item Predicate \texttt{price > 100}, row-group max = 80. What is the engine allowed to do?
  \item Why does projection pushdown (only read columns A, C) compose with predicate pushdown (skip rows by min/max), and how do they together reduce I/O multiplicatively?
\end{enumerate}

\section*{Build Plan}
\textbf{File: \texttt{minidaft/io/parquet.py}.}
\begin{lstlisting}
from dataclasses import dataclass, field
from typing import List, Optional, Iterator, Callable
import pyarrow as pa
from minidaft.plan import LogicalPlan

@dataclass(frozen=True)
class Pushdowns:
    """Carries pushed-down predicate, column list, and limit."""
    predicate: Optional[Callable] = None
    columns: Optional[List[str]] = None
    limit: Optional[int] = None

@dataclass
class ParquetScan(LogicalPlan):
    """A logical Source that reads Parquet with pushdowns applied."""
    path: str = ""
    pushdowns: Pushdowns = field(default_factory=Pushdowns)

    def execute(self) -> Iterator[pa.RecordBatch]:
        """Yield RecordBatches, skipping row groups whose min/max
        provably excludes the predicate."""
        ...
\end{lstlisting}

\begin{Hint}
APIs: \texttt{pyarrow.parquet.ParquetFile(path)}; \texttt{.metadata} for \texttt{FileMetaData}; \texttt{.metadata.row\_group(i)} for \texttt{RowGroupMetaData}; \texttt{.metadata.row\_group(i).column(j).statistics} exposes \texttt{has\_min\_max}, \texttt{min}, \texttt{max}, \texttt{null\_count} \cite{pyarrowparquet}; \texttt{.read\_row\_group(i, columns=[...])} returns a \texttt{pa.Table}; \texttt{table.to\_batches()} converts to a list of \texttt{RecordBatch}. Write a tiny fixture generator that produces a Parquet with 10 row groups via \texttt{pq.write\_table(..., row\_group\_size=N)}.
\end{Hint}

\section*{Tests}
File: \texttt{tests/test\_day3.py}. (i) Build a 10-row-group fixture in a tmp\_path fixture; with predicate that matches a single row group, assert the scan yields batches whose row count equals that row group's size. (ii) Instrument the scan with a counter; assert it called \texttt{read\_row\_group} exactly once. (iii) With projection \texttt{columns=["x"]}, assert returned schema has 1 field.

\section*{Comprehension Checks}
\begin{enumerate}
  \item Predicate \texttt{price > 100}, three row groups with maxima \{50, 120, 200\}. How many row groups are read?
  \item If a string column has many NULLs, why does \texttt{null\_count} statistics help even when min/max alone do not?
  \item Why is row-group pruning a property of the storage format, not of the engine?
\end{enumerate}

\section*{Pitfalls}
Statistics may be absent (\texttt{has\_min\_max == False}); when absent you \emph{must} read the row group. \texttt{read\_row\_group} returns a \texttt{Table}, not a \texttt{RecordBatch}. Pushdowns must be \emph{frozen} or you'll get aliasing across plan rewrites. Test fixtures must explicitly set \texttt{row\_group\_size}, else pyarrow writes a single row group and your test passes vacuously.

\section*{Definition of Done}
$\square$ 3 passing tests. $\square$ \texttt{ParquetScan(...).execute()} yields RecordBatches. $\square$ The decode counter test passes. $\square$ Committed.

\section*{Reflection}
What can a user of minidaft now do that they could not yesterday? Five sentences.

% =====================================================================
\chapter{Day 4 --- Optimizer Rules}

\section*{Orientation}
End of day: \texttt{optimize(plan)} applies \texttt{predicate\_pushdown}, \texttt{projection\_pushdown}, \texttt{filter\_combine}, \texttt{const\_fold} until a fixed point.

\section*{Read first}
\S4 of the textbook (rule-based optimization).

\section*{Intuition}
\begin{Analogy}
Optimizer rules are algebraic simplification. \texttt{2(x+3) - 6} becomes \texttt{2x} regardless of \texttt{x}. The plan tree is the expression; the rule is the simplification.
\end{Analogy}

Daft's optimizer applies ``classical rewrite rules \dots filter, projection, limit, and aggregation pushdowns; projection folding and splitting; pruning redundant repartitions; expression simplification; and subquery unnesting'' \cite{daftarch}. You are building a toy version of exactly this.

\section*{Leading Questions}
\begin{enumerate}
  \item Why is predicate pushdown a \emph{rewrite}, not a runtime decision?
  \item When can you \emph{not} push a filter through a project? Construct an example.
  \item Why does fixed-point iteration matter rather than a single pass?
\end{enumerate}

\section*{Build Plan}
\textbf{File: \texttt{minidaft/opt.py}.}
\begin{lstlisting}
from typing import Callable, List
from minidaft.plan import LogicalPlan

Rule = Callable[[LogicalPlan], LogicalPlan]

def optimize(plan: LogicalPlan, rules: List[Rule]) -> LogicalPlan:
    """Apply rules until fixed point. Returns a *new* plan tree;
    never mutates in place."""
    ...

def predicate_pushdown(plan: LogicalPlan) -> LogicalPlan:
    """Push Filter below Project when safe."""
    ...

def projection_pushdown(plan: LogicalPlan) -> LogicalPlan:
    """Push column lists down into ParquetScan.pushdowns.columns."""
    ...

def filter_combine(plan: LogicalPlan) -> LogicalPlan:
    """Filter(Filter(x, p), q) -> Filter(x, p AND q)."""
    ...

def const_fold(plan: LogicalPlan) -> LogicalPlan:
    """Lit(2) + Lit(3) -> Lit(5)."""
    ...
\end{lstlisting}

\begin{Hint}
Use \texttt{dataclasses.replace(node, child=new\_child)} to build a new node instead of mutating. Recursion: walk children first, then rewrite the current node. Fixed point: loop \texttt{while new\_plan != old\_plan}.
\end{Hint}

\section*{Tests}
File: \texttt{tests/test\_day4.py}. (i) \texttt{Filter(Project(Source, [x,y]), x>3)} optimizes to \texttt{Project(Filter(Source, x>3), [x,y])}. (ii) Two stacked Filters combine. (iii) \texttt{Lit(2)+Lit(3)} folds to \texttt{Lit(5)}. (iv) Projection pushdown lowers \texttt{["x","y"]} into the \texttt{ParquetScan}'s pushdowns.

\section*{Comprehension Checks}
\begin{enumerate}
  \item Why must rules return new nodes? What aliasing bug occurs if you mutate \texttt{children} in place?
  \item Give a concrete predicate that cannot be pushed through a UDF projection.
\end{enumerate}

\section*{Pitfalls}
Do \emph{not} mutate \texttt{plan.children} in place. Required vs.~defaulted fields: if you add fields to a dataclass subclass, the required ones must come before the defaulted ones --- or you'll see \texttt{TypeError: non-default argument follows default argument}. Forgetting \texttt{@dataclass} on a subclass strips its new fields. \texttt{types.py} (don't).

\section*{Definition of Done}
$\square$ 4 passing tests. $\square$ \texttt{.explain()} of an optimized plan shows the pushed-down structure. $\square$ Committed.

\section*{Reflection}
The user wrote one query and you ran a different (but equivalent) one. Why is that ethical?

% =====================================================================
\chapter{Day 5 --- Pull-Based Volcano Executor}

\section*{Orientation}
End of day: \texttt{df.where(\dots).select(\dots).limit(10).collect()} works end-to-end on a TPC-H \texttt{lineitem} Parquet subset.

\section*{Read first}
\S5 of the textbook (the Volcano iterator model, Graefe 1994 \cite{graefe1994volcano}).

\section*{Intuition}
\begin{Analogy}
A pull executor is a coffee shop with a single barista. The customer at the end of the line asks for a coffee. The barista asks the grinder for grounds. The grinder asks the bag for whole beans. Each step pulls from the previous. Nothing happens until the customer asks.
\end{Analogy}

\begin{Definition}[Volcano iterator]
Every operator implements \texttt{open()}, \texttt{next()} (returns one tuple or batch, or sentinel), and \texttt{close()}. The root pulls; the leaves source \cite{graefe1994volcano}.
\end{Definition}

\section*{Leading Questions}
\begin{enumerate}
  \item Why does a Volcano \texttt{Limit} naturally read only what it needs --- no special-casing required?
  \item What is the per-tuple overhead of \texttt{next()} being a virtual call, and why did Neumann argue it matters \cite{neumann2011compiling}?
  \item What is the cleanest way to plug an Arrow \texttt{compute.filter} into a tuple-at-a-time iterator? (Trick: batch-at-a-time \emph{is} the cleanest answer.)
\end{enumerate}

\section*{Build Plan}
\textbf{File: \texttt{minidaft/exec/pull.py}.}
\begin{lstlisting}
from typing import Iterator, Optional
import pyarrow as pa

class Executor:
    """Volcano-style. Each operator is an iterator of RecordBatch."""
    def open(self) -> None: ...
    def __iter__(self) -> Iterator[pa.RecordBatch]: ...
    def close(self) -> None: ...

class FilterExec(Executor):
    """Wraps a child executor, yields batches with predicate applied."""
    ...

class ProjectExec(Executor):
    """Yields batches with only the projected columns / new expressions."""
    ...

class LimitExec(Executor):
    """Yields up to n rows total, stops pulling early."""
    ...
\end{lstlisting}

\textbf{File: \texttt{minidaft/dataframe.py}.}
\begin{lstlisting}
class DataFrame:
    """Builder-pattern facade. Each method returns a *new* DataFrame
    with one more node added to the LogicalPlan; .collect() optimizes
    and executes."""
    def where(self, predicate) -> "DataFrame": ...
    def select(self, *exprs) -> "DataFrame": ...
    def limit(self, n: int) -> "DataFrame": ...
    def collect(self) -> pa.Table: ...
\end{lstlisting}

\begin{Hint}
APIs: \texttt{pyarrow.compute.filter(batch, mask)}, \texttt{pyarrow.compute.equal/greater/less/and\_/or\_}, Python generators (\texttt{yield}). The expression evaluator is a recursive walk of your \texttt{Expr} tree that returns a \texttt{pa.Array} per node.
\end{Hint}

\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=1.0cm,every node/.style={font=\small,draw,rounded corners,inner sep=3pt}]
\node (s) {Source};
\node[above=of s] (f) {Filter};
\node[above=of f] (p) {Project};
\node[above=of p] (l) {Limit};
\node[above=of l,draw=none] (c) {\textbf{collect()}};
\draw[->,dashed] (c) -- (l) node[midway,right]{pull};
\draw[->,dashed] (l) -- (p) node[midway,right]{pull};
\draw[->,dashed] (p) -- (f) node[midway,right]{pull};
\draw[->,dashed] (f) -- (s) node[midway,right]{pull};
\draw[->,thick] (s) to[bend left=50] (f);
\draw[->,thick] (f) to[bend left=50] (p);
\draw[->,thick] (p) to[bend left=50] (l);
\draw[->,thick] (l) to[bend left=50] (c);
\end{tikzpicture}
\caption{Volcano: dashed = control flow (consumer pulls), solid = data flow (producer returns).}
\end{figure}

\section*{Tests}
File: \texttt{tests/test\_day5.py}. (i) End-to-end: \texttt{DataFrame(parquet).where(price > 100).select(name).limit(10).collect()} returns 10 rows. (ii) Limit-early: a counter on the Source asserts you did not read the entire file. (iii) Filter result matches a pyarrow-only reference.

\section*{Comprehension Checks}
\begin{enumerate}
  \item Why does the pull model make \texttt{Limit(10)} efficient without any special optimizer rule?
  \item In your own words, what is the disadvantage of pull-based execution that the Daft team and DuckDB cite as motivation to switch to push?
\end{enumerate}

\section*{Pitfalls}
Generators are one-shot: re-running \texttt{.collect()} on the same DataFrame must rebuild iterators. Don't accidentally share a \texttt{pa.compute.field} expression --- it captures column-name state. Forgetting to close iterators leaks file handles.

\section*{Definition of Done}
$\square$ End-to-end test passes on a real Parquet file. $\square$ \texttt{.explain()} shows logical plan; an inverse method shows the physical executor tree. $\square$ Committed.

\section*{Reflection}
Explain the demand-driven nature of Volcano as if to a non-engineer. Five sentences.

% =====================================================================
\chapter{Day 6 --- Multimodal Types and Decode-Late}

\section*{Orientation}
End of day: an expression \texttt{col("url").url.download().image.decode()} runs, and the optimizer \emph{refuses} to push a predicate through it.

\section*{Read first}
\S6 of the textbook (multimodal data engines and the decode-late principle).

\section*{Intuition}
\begin{Analogy}
You have 10{,}000 rolls of film and need the cat photos. Naive: develop every roll, then look at each. Decode-late: read the metadata sticker first (``beach vacation''), skip the develop step for non-matching rolls entirely.
\end{Analogy}

Daft's optimizer ``intentionally [does] \emph{not} push [expensive projections] into scans so that execution can batch, schedule, and backpressure them independently. Such operations are executed as late as correctness permits (after joins, aggregations, etc.) to reduce wasted work on discarded rows'' \cite{daftarch}.

\section*{Leading Questions}
\begin{enumerate}
  \item What is the worst case for decoding eagerly when the downstream filter is highly selective?
  \item Why is ``decode-late'' the dual of ``predicate pushdown'' for cheap predicates --- you pull cheap ops down and push expensive ones up?
  \item If a UDF is marked expensive but actually cheap, what is the cost? If it is marked cheap but actually expensive, what is the cost?
\end{enumerate}

\section*{Build Plan}
\textbf{Modify: \texttt{minidaft/dtypes.py}} --- add \texttt{IMAGE\_BYTES}, \texttt{IMAGE\_DECODED}, \texttt{TENSOR}.

\textbf{Modify: \texttt{minidaft/expressions.py}} --- give \texttt{Expr} accessor properties \texttt{.url}, \texttt{.image} that return namespace objects whose methods (\texttt{download()}, \texttt{decode()}) construct \texttt{FnCall} nodes with \texttt{is\_expensive=True}.

\textbf{Modify: \texttt{minidaft/opt.py}} --- in \texttt{predicate\_pushdown}, refuse to push a predicate through a Project whose any expression is \texttt{is\_expensive=True}.

\begin{Hint}
APIs: \texttt{PIL.Image.open(io.BytesIO(b))}, \texttt{numpy.array(pil\_image)} for decoded tensor, \texttt{requests.get(url, timeout=...).content} for the download UDF. Wrap each decoder in an instrumentation counter for the test.
\end{Hint}

\section*{Tests}
File: \texttt{tests/test\_day6.py}. (i) Construct a plan \texttt{Filter(Project(Source, url.download.decode), category == "cat")} where Source has 1000 rows but 10 are cats. Assert the decoder counter equals \emph{1000} (decoded before filter, naively) when pushdown is disabled, and equals \emph{1000} or \emph{10} depending on rule. Actually: assert the optimizer refuses to push, so the order becomes Project-after-Filter --- and the decoder runs only 10 times. (ii) Assert a non-expensive UDF \emph{is} pushable.

\section*{Comprehension Checks}
\begin{enumerate}
  \item Why is image decoding marked expensive but \texttt{col("x") + 1} is not? Quantify.
  \item Daft talks about ``decode-late'' as an optimizer rule. What runtime mechanism (batching, backpressure) must also be in place for it to actually save resources \cite{daftarch}?
\end{enumerate}

\section*{Pitfalls}
Decorator namespaces (\texttt{.url}, \texttt{.image}) are easy to over-engineer; start with simple properties returning small helper classes. Don't make HTTP requests in unit tests --- use a local file:// URL or a tiny stub. Don't forget to type-tag \texttt{IMAGE\_BYTES} vs.~\texttt{IMAGE\_DECODED}; they are physically different.

\section*{Definition of Done}
$\square$ Decoder-count test passes. $\square$ Plan explainer prints \texttt{is\_expensive} flag. $\square$ Committed.

\section*{Reflection}
What is special about multimodal workloads (images, video, PDFs) that classical tabular optimizers ignore? Why is Eventual the company that figured this out?

% =====================================================================
\chapter{Day 7 --- Morsel-Driven Foundations}

\section*{Orientation}
End of day: a single-threaded \emph{push} driver that slices RecordBatches into morsels, pushes them through fused intermediate operators, and stops at a pipeline breaker. Result matches the pull executor on TPC-H \texttt{lineitem}.

\section*{Read first}
\S7 of the textbook (morsel-driven push-based parallelism). The Leis et al.~2014 paper \cite{leis2014morsel} is mandatory reading today.

\section*{Intuition}
\begin{Analogy}
A morsel is the bowl you hand to a sous-chef. Not a single onion (too granular, too many trips to the pantry), not the entire prep list (too coarse, blocks every other cook). A bowlful that fits on their station.
\end{Analogy}

\begin{Insight}
Leis et al.~write: ``We experimentally determined that a morsel size of about 100,000 tuples yields good tradeoff between instant elasticity adjustment, low scheduling overhead, and utilization of NUMA-local data'' \cite{leis2014morsel}. Their evaluation showed ``an average speedup of over 30 with 32 cores'' on TPC-H and SSB \cite{leis2014morsel}.
\end{Insight}

\begin{Definition}[Pipeline and pipeline breaker]
A \emph{pipeline} is a chain of operators that can run on one morsel without materializing intermediate results. A \emph{pipeline breaker} (e.g., a hash-join build side, an aggregate, a sort) must consume its entire input before its consumer pipeline starts \cite{leis2014morsel,neumann2011compiling}.
\end{Definition}

\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=0.9cm,every node/.style={font=\small,draw,rounded corners,inner sep=3pt}]
\node (s) {Source};
\node[right=of s] (f) {Filter};
\node[right=of f] (p) {Project};
\node[right=of p,fill=red!15] (a) {Aggregate (breaker)};
\node[right=of a] (snk) {Sink};
\draw[->] (s)--(f); \draw[->] (f)--(p); \draw[->,dashed] (p)--(a) node[midway,above,draw=none,font=\tiny]{materialize};
\draw[->] (a)--(snk);
\node[below=0.2cm of f,draw=none,font=\tiny\itshape] {Pipeline 1: morsel-at-a-time};
\node[below=0.2cm of snk,draw=none,font=\tiny\itshape] {Pipeline 2};
\end{tikzpicture}
\caption{Morsels flow through Pipeline 1 (Source-Filter-Project) into the breaker. Pipeline 2 starts only after the breaker is filled.}
\end{figure}

\section*{Leading Questions}
\begin{enumerate}
  \item Why are morsels sized in the \emph{thousands} of rows, not the millions and not single rows?
  \item In a push model, who calls whom? Who decides ``I'm done''?
  \item Why is the morsel framework JIT-friendly (Daft's Swordfish, HyPer's LLVM) in ways the Volcano iterator is not \cite{neumann2011compiling,daftswordfish}?
\end{enumerate}

\section*{Build Plan}
\textbf{File: \texttt{minidaft/exec/push.py}.}
\begin{lstlisting}
from dataclasses import dataclass
from typing import List, Optional
import pyarrow as pa

@dataclass
class Morsel:
    """A bounded slice of a RecordBatch, the unit of work."""
    batch: pa.RecordBatch
    seq: int  # ordering tag (matters for Limit)

class Pipeline:
    """A linear chain: Source -> [intermediate ops] -> Sink.
    Single-threaded driver loops over morsels, calling .push()
    on the next op."""
    def run(self) -> None: ...

class PushOp:
    """Each op receives a Morsel and emits zero or more Morsels."""
    def push(self, morsel: Morsel) -> List[Morsel]: ...
    def finalize(self) -> List[Morsel]: ...
\end{lstlisting}

\begin{Hint}
APIs: \texttt{pa.RecordBatch.slice(offset, length)} is zero-copy and is your morsel constructor. Choose a morsel size of, say, 8192 (rows) --- small enough that a Limit(1000) reads at most two morsels, large enough to amortize per-call overhead.
\end{Hint}

\section*{Tests}
File: \texttt{tests/test\_day7.py}. (i) Result-equality: the push pipeline result equals the pull executor's result on the same plan, batch-for-batch. (ii) Morsel-count test: with morsel size 1000 and a 10k-row file, the Source emitted exactly 10 morsels. (iii) Limit-with-push: \texttt{Limit(5)} on a 1M-row source emits only the first morsel.

\section*{Comprehension Checks}
\begin{enumerate}
  \item What happens if you set \texttt{morsel\_size = 1}? What if you set it to 10 million?
  \item Could you do morsel-driven execution \emph{without} push-based control flow? Why or why not? (Think: when does the consumer know it's done?)
  \item Daft's Swordfish ``adopts a Morsel-driven Push model'' and morsels are passed via ``async channels for streaming processing'' \cite{daftswordfish}. Why async channels rather than synchronous function calls?
\end{enumerate}

\section*{Pitfalls}
The morsel \texttt{seq} matters for Limit and Sort but not for stateless Project/Filter --- skip it for those. Don't forget \texttt{finalize()} on the sink; Aggregate's hash map only emits results when input is exhausted. Slicing a RecordBatch is zero-copy; \emph{do not} \texttt{combine\_chunks()} mid-pipeline.

\section*{Definition of Done}
$\square$ Result-equality test passes. $\square$ Morsel-count test passes. $\square$ Committed.

\section*{Reflection}
You implemented the same query two ways today (pull from Day 5, push today). Which felt more natural? Which was easier to make parallel? (Day 8 will answer the second question.)

% =====================================================================
\chapter{Day 8 --- Async Dispatcher with Work-Stealing}

\section*{Orientation}
End of day: an asyncio-based dispatcher with a global queue plus per-worker local deques. With \texttt{n\_workers=4}, an instrumented run confirms all 4 workers received morsels.

\section*{Read first}
\S3 of \cite{leis2014morsel} (the dispatcher and work-stealing). Daft's Swordfish runs on Tokio with ``a multithreaded work scheduler'' \cite{daftswordfish}; you are building the Python analogue.

\section*{Intuition}
\begin{Analogy}
Work-stealing is a kitchen where idle cooks help busy ones. Each cook has their own ticket queue; when their queue is empty they peek at a neighbor's and grab a ticket from the bottom of the pile (so the neighbor keeps working on the top).
\end{Analogy}

\begin{Insight}[Honest GIL accounting]
In pure Python, asyncio gives you \emph{concurrency}, not \emph{parallelism}. You will demonstrate the work-stealing \emph{control structure} faithfully; wall-clock parallelism comes from the pyarrow C kernels and from \texttt{asyncio} interleaving I/O with compute. Daft solves this for real by writing the engine in Rust \cite{daftarch,daftswordfish}.
\end{Insight}

\section*{Leading Questions}
\begin{enumerate}
  \item Why steal from the \emph{bottom} of a neighbor's deque, not the top?
  \item Why is a \emph{bounded} \texttt{asyncio.Queue} the simplest form of backpressure?
  \item What does ``elasticity'' mean in the Leis dispatcher \cite{leis2014morsel}, and is it the same as ``autoscaling''?
\end{enumerate}

\section*{Build Plan}
\textbf{File: \texttt{minidaft/exec/dispatcher.py}.}
\begin{lstlisting}
import asyncio
from collections import deque
from dataclasses import dataclass, field
from typing import List, Deque

@dataclass
class Dispatcher:
    """Global queue + per-worker deques; workers steal when local is empty."""
    n_workers: int
    global_q: asyncio.Queue
    local: List[Deque] = field(default_factory=list)
    locks: List[asyncio.Lock] = field(default_factory=list)

    async def worker(self, wid: int, sink) -> None:
        """Worker loop: drain local deque, else pop global, else steal."""
        ...

    async def run(self, source, sink) -> None:
        """Spawn n_workers and await them all."""
        ...
\end{lstlisting}

\begin{Hint}
APIs: \texttt{asyncio.Queue(maxsize=N)} for the global queue and for backpressure; \texttt{asyncio.gather(*tasks)} to await all workers; \texttt{collections.deque} for per-worker local; \texttt{asyncio.Lock} when stealing across deques; \texttt{asyncio.Semaphore(max\_inflight)} if you want a cap on concurrent expensive UDFs.
\end{Hint}

\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=0.7cm,every node/.style={font=\small,draw,rounded corners,inner sep=3pt}]
\node (g) {Global Queue};
\node[below left=1.2cm and 1.5cm of g] (w1) {Worker 0};
\node[below=1.2cm of g] (w2) {Worker 1};
\node[below right=1.2cm and 1.5cm of g] (w3) {Worker 2};
\node[below=of w1] (d1) {deque 0};
\node[below=of w2] (d2) {deque 1};
\node[below=of w3] (d3) {deque 2};
\draw[->] (g)--(w1); \draw[->] (g)--(w2); \draw[->] (g)--(w3);
\draw[<->] (w1)--(d1); \draw[<->] (w2)--(d2); \draw[<->] (w3)--(d3);
\draw[->,dashed,red] (d1) to[bend left=20] node[midway,above,draw=none,font=\tiny,red]{steal} (w3);
\end{tikzpicture}
\caption{Workers prefer local deques; steal from a neighbor's bottom when both local and global are empty.}
\end{figure}

\section*{Tests}
File: \texttt{tests/test\_day8.py}. (i) With 4 workers and 100 morsels, each worker recorded $\ge 1$ morsel processed. (ii) Backpressure: set queue maxsize=2; assert producer awaited (use a timestamp diff). (iii) Result-equality with Day 7 single-threaded push.

\section*{Comprehension Checks}
\begin{enumerate}
  \item Daft's Flotilla runs ``one Swordfish worker per node'' \cite{daftarch,daftflotilla}. How is that the same idea as your dispatcher, scaled up one level?
  \item Why is morsel-driven dispatch ``fully elastic'' --- ``the dispatcher can react to execution speed of different morsels but also adjust resources dynamically'' \cite{leis2014morsel}?
\end{enumerate}

\section*{Pitfalls}
\texttt{asyncio.Queue} is \emph{not} thread-safe --- use it only within one event loop. Forgetting \texttt{await} silently returns a coroutine. \texttt{asyncio.gather} propagates the first exception and cancels the rest --- wrap workers in try/except if you want partial-failure semantics. Don't use \texttt{time.sleep} in an async coroutine; use \texttt{await asyncio.sleep}.

\section*{Definition of Done}
$\square$ 3 passing tests. $\square$ Per-worker counter logged in instrumented mode. $\square$ Committed.

\section*{Reflection}
The Eventual interviewer asks: ``What's the limitation of your Python dispatcher and how would Rust + Tokio fix it?'' Write the answer in five sentences \cite{daftswordfish}.

% =====================================================================
\chapter{Day 9 --- Pipeline Breakers and Backpressure}

\section*{Orientation}
End of day: \texttt{Aggregate} (blocking sink with thread-local partial dicts then global combine), \texttt{Sort} (parallel merge), \texttt{Limit} (streaming sink with sender-drop). Verify that a \texttt{Limit(5)} on a 1M-row file does \emph{not} read the full dataset.

\section*{Read first}
\S4 of \cite{leis2014morsel} (parallel join/aggregation/sort). Daft's architecture: ``Streaming sinks (e.g.~Limit) can emit early, while blocking sinks (e.g.~Aggregate, Sort) only emit results once all input has been processed'' \cite{daftarch}.

\section*{Intuition}
\begin{Analogy}
A pipeline breaker is the moment in cooking when you stop and wait --- you can't plate a reduction sauce until it has fully reduced. Aggregate is the reduction. Limit is ``that's enough, throw out the rest'' --- a streaming sink that signals upstream to halt.
\end{Analogy}

\section*{Leading Questions}
\begin{enumerate}
  \item Why does \texttt{Aggregate} need partial-then-combine to scale across workers, but \texttt{Filter} does not?
  \item How does a streaming \texttt{Limit} signal the source to stop? (Answer in terms of channels.)
  \item Why is sorting (a blocking sink) more expensive in memory than aggregation?
\end{enumerate}

\section*{Build Plan}
\textbf{File: \texttt{minidaft/exec/sinks.py}.}
\begin{lstlisting}
from collections import defaultdict
import heapq
from typing import Dict, List
import pyarrow as pa

class AggregateSink:
    """Blocking. Thread-local partial dicts then global combine."""
    partials: List[Dict]  # one per worker
    def push(self, morsel) -> None: ...
    def finalize(self) -> pa.Table: ...

class SortSink:
    """Blocking. Each worker sorts its received morsels; finalize
    does a k-way merge."""
    def push(self, morsel) -> None: ...
    def finalize(self) -> pa.Table: ...

class LimitSink:
    """Streaming. Counts rows; when n reached, closes its inbound
    channel so producer naturally exits."""
    def push(self, morsel) -> List["Morsel"]: ...
\end{lstlisting}

\begin{Hint}
APIs: \texttt{collections.defaultdict(int)} for hash aggregation; \texttt{heapq.merge(*sorted\_iterables, key=...)} for parallel merge; close an \texttt{asyncio.Queue} by calling \texttt{q.put\_nowait(SENTINEL)} or by cancelling the producer task.
\end{Hint}

\section*{Tests}
File: \texttt{tests/test\_day9.py}. (i) Aggregate sum-by-group on 1M synthetic rows matches a pandas reference. (ii) Limit(5) test instruments the Source row count; assert source emitted $\le$ \texttt{morsel\_size + 5} rows. (iii) Sort produces globally sorted output.

\section*{Comprehension Checks}
\begin{enumerate}
  \item Daft's optimizer ``defers expensive projections after joins, aggregations, etc.~to reduce wasted work on discarded rows'' \cite{daftarch}. Compose that statement with your Day 6 decode-late rule. Why is the order Filter $\to$ Aggregate $\to$ Decode the right one for an image-classification pipeline?
  \item Why is \texttt{heapq.merge} the right primitive for parallel merge sort, not \texttt{sorted}?
\end{enumerate}

\section*{Pitfalls}
Aggregate's global combine must handle empty per-worker partials. Sort's merge requires per-worker outputs to already be sorted --- enforce that in \texttt{push}. Limit's sender-drop must use a sentinel or cancellation; never a bare \texttt{return} from a producer holding a queue slot.

\section*{Definition of Done}
$\square$ 3 sink tests pass. $\square$ Limit-early test demonstrably reads $< 1\%$ of the file. $\square$ Committed.

\section*{Reflection}
What is the difference between a streaming sink and a blocking sink, in 4 sentences with no jargon?

% =====================================================================
\chapter{Day 10 --- Benchmark and Polish}

\section*{Orientation}
End of day: an end-to-end multimodal benchmark on a LAION-Aesthetics 10k subset (filter \texttt{aesthetic\_score > 6.0}, download, decode, resize to 224, embed via a stub UDF). Three measurements: peak RSS, wall clock, decode count. Baseline: pandas + PIL + \texttt{requests} loops. A README with architecture diagram and a 60-second screen recording.

\section*{Read first}
\S10 of the textbook (benchmarking methodology). Skim the Daft benchmark blog \cite{daftbench} and the Flotilla post \cite{daftflotilla} so your README sounds informed.

\section*{Intuition}
\begin{Analogy}
A benchmark is the photo at the end of the hike --- proof that the path you walked exists, that someone else could walk it, and that it really goes where you say it does.
\end{Analogy}

Daft's Flotilla paper, written by Colin Ho and published on the daft.ai blog on 1 October 2025, validates Daft on ``four real-world multimodal pipelines: audio transcription, document embedding, image classification, and video object detection'' and reports that ``Daft with Flotilla ran 2-7x faster than Ray Data and 4-18x faster than Spark, while using smaller clusters and completing without crashes'' \cite{daftflotilla}. Your benchmark is a kitchen-table miniature of that.

\section*{Leading Questions}
\begin{enumerate}
  \item What three numbers tell the whole story of a streaming multimodal engine? Why those three?
  \item Why is the \emph{baseline} (pandas + PIL + \texttt{requests} loops) the right comparator, not pyspark?
  \item What is the cheapest way to lie with a benchmark, and how do you not do it?
\end{enumerate}

\section*{Build Plan}
\textbf{File: \texttt{bench/laion\_bench.py}.}
\begin{lstlisting}
import time, os, psutil
import matplotlib.pyplot as plt
from minidaft.dataframe import DataFrame

def run_minidaft(parquet_path: str) -> dict:
    """Returns {'wall_s': ..., 'peak_rss_mb': ..., 'decode_count': ...}."""
    ...

def run_baseline(parquet_path: str) -> dict:
    """Pandas + PIL + requests loop, same logical query."""
    ...
\end{lstlisting}

\begin{Hint}
APIs: \texttt{psutil.Process(os.getpid()).memory\_info().rss} (sample every 0.1s in a daemon thread); \texttt{time.perf\_counter()} bracketing the work; \texttt{matplotlib.pyplot.bar} for a three-bar plot of \{wall, RSS, decode\}. Limit the LAION subset to 10k rows so the bench runs in $\le 10$ minutes on your laptop. The LAION-Aesthetics subset is documented at \cite{laionaesthetics}.
\end{Hint}

\section*{Tests}
File: \texttt{tests/test\_day10.py}. (i) Both runners produce identical row counts and identical aggregate stats. (ii) The decode counter for minidaft equals the post-filter row count (decode-late from Day 6 still holds end-to-end). (iii) Peak RSS for minidaft is at most $0.5\times$ baseline (streaming saved memory).

\section*{Comprehension Checks}
\begin{enumerate}
  \item Daft v0.7.6 introduced ``fingerprint-based plan caching in Swordfish'' so ``multiple executions of the same logical plan now share a single pipeline instead of building a new one each time'' \cite{daftv076}. What benchmark axis would catch the win from plan caching, that your three numbers do not?
  \item If your peak RSS is \emph{higher} than the baseline, what is the bug? (Hint: think about morsel size and how many morsels are in flight simultaneously when the dispatcher has 4 workers.)
\end{enumerate}

\section*{Pitfalls}
Network variance dominates if you re-download images per run --- cache locally on first run. RSS-via-\texttt{psutil} samples are noisy; take the max of $\sim$100 samples. Do not benchmark with debug logging on. The first run is always slower (file-cache cold); discard it.

\section*{Definition of Done}
$\square$ Bench script runs end-to-end. $\square$ README contains: (a) one-paragraph elevator pitch, (b) architecture diagram (use \texttt{tikz} or a hand drawing), (c) the three-bar plot, (d) a 200-word ``why decode-late matters'' section citing \cite{daftarch}, (e) link to a 60-second screen recording of the bench running. $\square$ Final commit \texttt{Day 10: benchmark and polish}.

\section*{Reflection}
Jay asks at the on-site: ``Walk me through what you built in ten days, and why.'' Write the answer in one paragraph (8-10 sentences). No jargon. End with one sentence about what you would build on Day 11 if you had one more day.

% =====================================================================
\chapter*{Closing Note: What You Now Hold in Your Head}
\addcontentsline{toc}{chapter}{Closing Note}

You have, in ten days, walked the same conceptual path that took the Daft team from a logical-plan IR to a streaming push-based morsel-driven multimodal engine. Your version is in Python and your dispatcher is GIL-bound; Daft's is in Rust on Tokio with a real work-scheduler \cite{daftswordfish,daftarch}. But the \emph{ideas} --- the two nested trees, the pull-then-push transition, the morsel as the unit of work, the pipeline breaker, the decode-late rule, the streaming \texttt{Limit} that closes its channel upstream --- are the same ideas. When Jay walks you through Daft's repo at the on-site \cite{daftrepo}, you will not be reading hieroglyphics; you will be reading the language you spent ten days speaking.

Good luck.

\backmatter
\printbibliography[heading=bibintoc,title={References}]

\end{document}