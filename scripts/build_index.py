#!/usr/bin/env python3
"""Generate index/roster.csv, index/quarantine.csv and index/unsolved-cases.csv.

The roster is the project's list of admissible subjects. An entry may only be
added here after a maintainer has corroborated (a) that the person exists,
(b) that they were convicted, and (c) that the case meets the inclusion
criteria in docs/inclusion-criteria.md.

Entries that fail any of those checks go to quarantine.csv with a reason.
Nothing moves from quarantine to roster without a citable source.
"""

import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "index"

# ---------------------------------------------------------------------------
# ROSTER — subjects cleared for profiling.
# (id, name, iso3, epithet, classification, status)
#
# classification: serial | healthcare | poisoner
#
# There is no 'team' classification. Offenders who acted together each get
# their own record, linked by the profile schema's `co_offenders` field.
# See docs/co-offenders.md.
# status: stub (no profile yet) | in_progress | complete
# ---------------------------------------------------------------------------

ROSTER = [
    # --- United States -----------------------------------------------------
    # USA-011-CORLL is a CASE record (died before trial), not a roster entry.
    ("USA-001-BUNDY",      "Theodore Robert Bundy",        "USA", "", "serial", "in_progress"),
    ("USA-002-RIDGWAY",    "Gary Leon Ridgway",            "USA", "Green River Killer", "serial", "in_progress"),
    ("USA-004-DEANGELO",   "Joseph James DeAngelo Jr.",    "USA", "Golden State Killer", "serial", "in_progress"),
    ("USA-005-GACY",       "John Wayne Gacy",              "USA", "The Killer Clown", "serial", "in_progress"),
    ("USA-006-RADER",      "Dennis Lynn Rader",            "USA", "BTK", "serial", "in_progress"),
    ("USA-007-DAHMER",     "Jeffrey Lionel Dahmer",        "USA", "", "serial", "in_progress"),
    ("USA-008-RAMIREZ",    "Richard Ramirez",              "USA", "Night Stalker", "serial", "in_progress"),
    ("USA-009-KEMPER",     "Edmund Emil Kemper III",       "USA", "Co-Ed Killer", "serial", "in_progress"),
    ("USA-010-BERKOWITZ",  "David Richard Berkowitz",      "USA", "Son of Sam", "serial", "in_progress"),
    ("USA-012-HENLEY",     "Elmer Wayne Henley Jr.",       "USA", "", "serial", "in_progress"),
    ("USA-013-BROOKS",     "David Owen Brooks",            "USA", "", "serial", "in_progress"),
    ("USA-014-BITTAKER",   "Lawrence Sigmond Bittaker",    "USA", "", "serial", "stub"),
    ("USA-015-NORRIS",     "Roy Lewis Norris",             "USA", "", "serial", "stub"),
    ("USA-016-BIANCHI",    "Kenneth Alessio Bianchi",      "USA", "Hillside Strangler", "serial", "stub"),
    ("USA-017-BUONO",      "Angelo Buono Jr.",             "USA", "Hillside Strangler", "serial", "stub"),
    ("USA-018-NG",         "Charles Chitat Ng",            "USA", "", "serial", "stub"),
    # USA-019-LAKE is a CASE record (died before trial).
    ("USA-020-DESALVO",    "Albert Henry DeSalvo",         "USA", "Boston Strangler", "serial", "stub"),
    ("USA-021-ALCALA",     "Rodney James Alcala",          "USA", "", "serial", "stub"),
    ("USA-022-LITTLE",     "Samuel Little",                "USA", "", "serial", "stub"),
    ("USA-023-HOLMES",     "Herman Webster Mudgett",       "USA", "H. H. Holmes", "serial", "stub"),
    ("USA-024-SHAWCROSS",  "Arthur John Shawcross",        "USA", "", "serial", "stub"),
    ("USA-025-CHASE",      "Richard Trenton Chase",        "USA", "", "serial", "stub"),
    ("USA-026-KEARNEY",    "Patrick Wayne Kearney",        "USA", "", "serial", "stub"),
    ("USA-027-WILLIAMS",   "Wayne Bertram Williams",       "USA", "", "serial", "stub"),
    ("USA-028-GASKINS",    "Donald Henry Gaskins",         "USA", "", "serial", "stub"),
    ("USA-029-STANO",      "Gerald Eugene Stano",          "USA", "", "serial", "stub"),
    ("USA-030-DOMINIQUE",  "Ronald Joseph Dominique",      "USA", "", "serial", "stub"),
    ("USA-031-LEE",        "Derrick Todd Lee",             "USA", "", "serial", "stub"),
    ("USA-032-WATTS",      "Carl Eugene Watts",            "USA", "", "serial", "stub"),
    ("USA-033-HANSEN",     "Robert Christian Hansen",      "USA", "", "serial", "stub"),
    ("USA-034-KRAFT",      "Randy Steven Kraft",           "USA", "", "serial", "stub"),
    ("USA-035-BONIN",      "William George Bonin",         "USA", "Freeway Killer", "serial", "stub"),
    ("USA-036-HEIDNIK",    "Gary Michael Heidnik",         "USA", "", "serial", "stub"),
    ("USA-037-HATCHER",    "Charles Ray Hatcher",          "USA", "", "serial", "stub"),
    # USA-038-KEYES is a CASE record (died before trial).
    ("USA-039-FRANKLIN",   "Lonnie David Franklin Jr.",    "USA", "Grim Sleeper", "serial", "stub"),
    ("USA-040-JESPERSON",  "Keith Hunter Jesperson",       "USA", "Happy Face Killer", "serial", "stub"),
    ("USA-041-SELLS",      "Tommy Lynn Sells",             "USA", "", "serial", "stub"),
    ("USA-042-LUCAS",      "Henry Lee Lucas",              "USA", "", "serial", "stub"),
    ("USA-043-TOOLE",      "Ottis Elwood Toole",           "USA", "", "serial", "stub"),
    ("USA-044-CORONA",     "Juan Vallejo Corona",          "USA", "", "serial", "stub"),
    ("USA-045-RAY",        "David Parker Ray",             "USA", "Toy-Box Killer", "serial", "stub"),
    ("USA-046-RUSSELL",    "George Waterfield Russell Jr.","USA", "", "serial", "stub"),
    ("USA-047-ROSS",       "Michael Bruce Ross",           "USA", "", "serial", "stub"),
    ("USA-048-ROLLING",    "Danny Harold Rolling",         "USA", "Gainesville Ripper", "serial", "stub"),
    ("USA-049-ATKINS",     "Benjamin Tyrone Atkins",       "USA", "", "serial", "stub"),
    ("USA-050-JFRANKLIN",  "Joseph Paul Franklin",         "USA", "", "serial", "stub"),
    ("USA-051-ROGERS",     "Richard W. Rogers",            "USA", "Last Call Killer", "serial", "stub"),
    ("USA-052-FRANCOIS",   "Kendall L. Francois",          "USA", "", "serial", "stub"),
    ("USA-053-GILYARD",    "Lorenzo Jerome Gilyard",       "USA", "", "serial", "stub"),
    ("USA-054-KNOWLES",    "Paul John Knowles",            "USA", "", "serial", "stub"),
    ("USA-055-TRAVIS",     "Maury Troy Travis",            "USA", "", "serial", "stub"),
    ("USA-056-TURNER",     "Chester Dewayne Turner",       "USA", "", "serial", "stub"),
    ("USA-057-NASO",       "Joseph Naso",                  "USA", "", "serial", "stub"),
    ("USA-058-BIRD",       "Jake Bird",                    "USA", "", "serial", "stub"),
    ("USA-059-DOSS",       "Nannie Doss",                  "USA", "", "poisoner", "stub"),
    ("USA-060-GUNNESS",    "Belle Gunness",                "USA", "", "serial", "stub"),
    ("USA-061-ARCHER",     "Amy Archer-Gilligan",          "USA", "", "healthcare", "stub"),
    ("USA-062-WILDER",     "Christopher Bernard Wilder",   "USA", "", "serial", "stub"),
    ("USA-063-KUKLINSKI",  "Richard Leonard Kuklinski",    "USA", "", "serial", "stub"),
    ("USA-064-SOTO",       "Erno Soto",                    "USA", "", "serial", "stub"),

    # --- Canada ------------------------------------------------------------
    ("CAN-001-PICKTON",    "Robert William Pickton",       "CAN", "", "serial", "stub"),
    ("CAN-002-OLSON",      "Clifford Robert Olson Jr.",    "CAN", "", "serial", "stub"),
    ("CAN-003-BERNARDO",   "Paul Kenneth Bernardo",        "CAN", "", "serial", "stub"),
    ("CAN-004-HOMOLKA",    "Karla Leanne Homolka",         "CAN", "", "serial", "stub"),
    ("CAN-005-DION",       "Léopold Dion",                 "CAN", "", "serial", "stub"),
    ("CAN-006-JORDAN",     "Gilbert Paul Jordan",          "CAN", "", "serial", "stub"),
    ("CAN-007-BODEN",      "Wayne Clifford Boden",         "CAN", "", "serial", "stub"),
    ("CAN-008-LEGERE",     "Allan Joseph Legere",          "CAN", "", "serial", "stub"),
    ("CAN-009-FYFE",       "William Patrick Fyfe",         "CAN", "", "serial", "stub"),
    ("CAN-010-MCGRAY",     "Michael Wayne McGray",         "CAN", "", "serial", "stub"),
    ("CAN-011-WETTLAUFER", "Elizabeth Tracey Mae Wettlaufer","CAN","", "healthcare", "stub"),
    ("CAN-012-MCARTHUR",   "Bruce McArthur",               "CAN", "", "serial", "stub"),

    # --- Mexico ------------------------------------------------------------
    ("MEX-001-BARRAZA",    "Juana Barraza",                "MEX", "La Mataviejitas", "serial", "stub"),
    ("MEX-002-RESENDIZ",   "Ángel Maturino Reséndiz",      "MEX", "Railroad Killer", "serial", "stub"),

    # --- France ------------------------------------------------------------
    ("FRA-001-VEROVE",     "François Vérove",              "FRA", "Le Grêlé", "serial", "stub"),
    ("FRA-002-FOURNIRET",  "Michel Fourniret",             "FRA", "", "serial", "stub"),
    ("FRA-003-GEORGES",    "Guy Georges",                  "FRA", "", "serial", "stub"),
    ("FRA-004-ALEGRE",     "Patrice Alègre",               "FRA", "", "serial", "stub"),
    ("FRA-005-PETIOT",     "Marcel Petiot",                "FRA", "", "serial", "stub"),
    ("FRA-006-LANDRU",     "Henri Désiré Landru",          "FRA", "", "serial", "stub"),
    ("FRA-007-LOUIS",      "Émile Louis",                  "FRA", "", "serial", "stub"),
    ("FRA-008-HEAULME",    "Francis Heaulme",              "FRA", "", "serial", "stub"),
    ("FRA-009-KELLER",     "Yvan Keller",                  "FRA", "", "serial", "stub"),

    # --- United Kingdom ----------------------------------------------------
    ("GBR-001-SUTCLIFFE",  "Peter William Sutcliffe",      "GBR", "Yorkshire Ripper", "serial", "stub"),
    ("GBR-002-BRADY",      "Ian Brady",                    "GBR", "Moors Murderers", "serial", "stub"),
    ("GBR-003-HINDLEY",    "Myra Hindley",                 "GBR", "Moors Murderers", "serial", "stub"),
    # GBR-004-FWEST is a CASE record (died on remand, before trial).
    ("GBR-005-RWEST",      "Rosemary Pauline West",        "GBR", "", "serial", "stub"),
    ("GBR-006-NILSEN",     "Dennis Andrew Nilsen",         "GBR", "", "serial", "stub"),
    ("GBR-007-SHIPMAN",    "Harold Frederick Shipman",     "GBR", "", "healthcare", "stub"),
    ("GBR-008-CHRISTIE",   "John Reginald Halliday Christie","GBR","", "serial", "stub"),
    ("GBR-009-HAIGH",      "John George Haigh",            "GBR", "Acid Bath Murderer", "serial", "stub"),
    ("GBR-010-BLACK",      "Robert Black",                 "GBR", "", "serial", "stub"),
    ("GBR-011-TOBIN",      "Peter Britton Tobin",          "GBR", "", "serial", "stub"),
    ("GBR-012-IRELAND",    "Colin Ireland",                "GBR", "", "serial", "stub"),
    ("GBR-013-MACKAY",     "Patrick David Mackay",         "GBR", "", "serial", "stub"),
    ("GBR-014-SCRIPPS",    "John Martin Scripps",          "GBR", "", "serial", "stub"),

    # --- Belgium -----------------------------------------------------------
    ("BEL-001-DUTROUX",    "Marc Dutroux",                 "BEL", "", "serial", "stub"),

    # --- Germany -----------------------------------------------------------
    ("DEU-001-KURTEN",     "Peter Kürten",                 "DEU", "Vampire of Düsseldorf", "serial", "stub"),
    ("DEU-002-HAARMANN",   "Friedrich Heinrich Karl Haarmann","DEU","", "serial", "stub"),
    ("DEU-003-KROLL",      "Joachim Georg Kroll",          "DEU", "", "serial", "stub"),
    ("DEU-004-HOLST",      "Thomas Holst",                 "DEU", "Heidemörder", "serial", "stub"),
    ("DEU-005-LETTER",     "Stephan Letter",               "DEU", "", "healthcare", "stub"),
    ("DEU-006-HOEGEL",     "Niels Högel",                  "DEU", "", "healthcare", "stub"),

    # --- Austria / Switzerland --------------------------------------------
    ("AUT-001-UNTERWEGER", "Johann Jack Unterweger",       "AUT", "", "serial", "stub"),
    ("CHE-001-PEIRY",      "Michel Peiry",                 "CHE", "Le sadique de Romont", "serial", "stub"),

    # --- Russia / former USSR ---------------------------------------------
    ("RUS-001-CHIKATILO",  "Andrei Romanovich Chikatilo",  "RUS", "", "serial", "stub"),
    ("RUS-002-PICHUSHKIN", "Alexander Yuryevich Pichushkin","RUS","Chessboard Killer", "serial", "stub"),
    ("RUS-003-POPKOV",     "Mikhail Viktorovich Popkov",   "RUS", "", "serial", "stub"),
    ("RUS-004-SLIVKO",     "Anatoly Yemelianovich Slivko", "RUS", "", "serial", "stub"),
    ("RUS-005-DZHUMA",     "Nikolai Dzhumagaliev",         "RUS", "", "serial", "stub"),
    ("RUS-006-PETROV",     "Maxim Petrov",                 "RUS", "", "healthcare", "stub"),
    ("RUS-007-TAGIROV",    "Radik Tagirov",                "RUS", "", "serial", "stub"),
    ("BLR-001-MIKHASEVICH","Gennady Mikhasevich",          "BLR", "Vitebsk Strangler", "serial", "stub"),
    ("UKR-001-ONOPRIENKO", "Anatoly Yuriyovych Onoprienko","UKR", "", "serial", "stub"),
    ("UKR-002-TKACH",      "Serhiy Tkach",                 "UKR", "", "serial", "stub"),

    # --- Italy / Spain / Nordics ------------------------------------------
    ("ITA-001-BILANCIA",   "Donato Bilancia",              "ITA", "", "serial", "stub"),
    ("ITA-002-MINGHELLA",  "Maurizio Minghella",           "ITA", "", "serial", "stub"),
    ("ESP-001-ROMASANTA",  "Manuel Blanco Romasanta",      "ESP", "", "serial", "stub"),
    ("ESP-002-VEGA",       "José Antonio Rodríguez Vega",  "ESP", "", "serial", "stub"),
    ("ESP-003-ESCALERO",   "Francisco García Escalero",    "ESP", "", "serial", "stub"),
    ("DNK-001-OVERBYE",    "Dagmar Overbye",               "DNK", "", "serial", "stub"),
    ("SWE-001-AUSONIUS",   "John Ausonius",                "SWE", "Laser Man", "serial", "stub"),

    # --- South America -----------------------------------------------------
    ("COL-001-GARAVITO",   "Luis Alfredo Garavito Cubillos","COL","La Bestia", "serial", "stub"),
    ("COL-002-LOPEZ",      "Pedro Alonso López",           "COL", "", "serial", "stub"),
    ("COL-003-CAMARGO",    "Daniel Camargo Barbosa",       "COL", "", "serial", "stub"),
    ("BRA-001-FILHO",      "Pedro Rodrigues Filho",        "BRA", "", "serial", "stub"),
    ("BRA-002-ROCHA",      "Tiago Henrique Gomes da Rocha","BRA", "", "serial", "stub"),
    ("BRA-003-PEREIRA",    "Francisco de Assis Pereira",   "BRA", "Park Maniac", "serial", "stub"),
    ("ARG-001-GODINO",     "Cayetano Santos Godino",       "ARG", "El Petiso Orejudo", "serial", "stub"),
    ("ARG-002-PUCH",       "Carlos Eduardo Robledo Puch",  "ARG", "", "serial", "stub"),
    ("ARG-003-MURANO",     "Yiya Murano",                  "ARG", "", "poisoner", "stub"),
    ("VEN-001-VARGAS",     "Dorángel Vargas",              "VEN", "", "serial", "stub"),

    # --- Asia --------------------------------------------------------------
    ("PAK-001-IQBAL",      "Javed Iqbal",                  "PAK", "", "serial", "stub"),
    ("PAK-002-QAYYUM",     "Amir Qayyum",                  "PAK", "", "serial", "stub"),
    ("JPN-001-MIYAZAKI",   "Tsutomu Miyazaki",             "JPN", "", "serial", "stub"),
    ("JPN-002-KATSUTA",    "Kiyotaka Katsuta",             "JPN", "", "serial", "stub"),
    ("JPN-003-MATSUNAGA",  "Futoshi Matsunaga",            "JPN", "", "serial", "stub"),
    ("JPN-004-SHIRAISHI",  "Takahiro Shiraishi",           "JPN", "", "serial", "stub"),
    ("KOR-001-YOO",        "Yoo Young-chul",               "KOR", "", "serial", "stub"),
    ("KOR-002-LEE",        "Lee Choon-jae",                "KOR", "", "serial", "stub"),
    ("KOR-003-KANG",       "Kang Ho-sun",                  "KOR", "", "serial", "stub"),
    ("CHN-001-YANG",       "Yang Xinhai",                  "CHN", "", "serial", "stub"),
    ("CHN-002-GAO",        "Gao Chengyong",                "CHN", "", "serial", "stub"),
    ("CHN-003-ZHANG",      "Zhang Yongming",               "CHN", "", "serial", "stub"),
    ("HKG-001-LAM",        "Lam Kor-wan",                  "HKG", "", "serial", "stub"),
    ("IND-001-RAGHAV",     "Raman Raghav",                 "IND", "", "serial", "stub"),
    ("IND-002-KUMAR",      "Mohan Kumar",                  "IND", "Cyanide Mohan", "poisoner", "stub"),
    ("IND-003-JAISHANKAR", "Mohan Jaishankar",             "IND", "", "serial", "stub"),
    ("IDN-001-SURADJI",    "Ahmad Suradji",                "IDN", "", "serial", "stub"),
    ("IRN-001-BIJEH",      "Mohammad Bijeh",               "IRN", "", "serial", "stub"),

    # --- Africa ------------------------------------------------------------
    ("ZAF-001-SITHOLE",    "Moses Sithole",                "ZAF", "ABC Killer", "serial", "stub"),
    ("ZAF-002-MAAKE",      "Cedric Maake",                 "ZAF", "", "serial", "stub"),
    ("ZAF-003-WILKEN",     "Stewart Wilken",               "ZAF", "Boetie Boer", "serial", "stub"),

    # --- Oceania -----------------------------------------------------------
    ("AUS-001-MILAT",      "Ivan Robert Marko Milat",      "AUS", "Backpacker Killer", "serial", "stub"),
    ("AUS-002-COOKE",      "Eric Edgar Cooke",             "AUS", "", "serial", "stub"),
    ("AUS-003-BUNTING",    "John Justin Bunting",          "AUS", "Snowtown", "serial", "stub"),
    ("AUS-004-DBIRNIE",    "David John Birnie",            "AUS", "", "serial", "stub"),
    ("AUS-005-CBIRNIE",    "Catherine Margaret Birnie",    "AUS", "", "serial", "stub"),
    ("AUS-006-MACDONALD",  "William MacDonald",            "AUS", "", "serial", "stub"),
    ("AUS-007-DENYER",     "Paul Charles Denyer",          "AUS", "", "serial", "stub"),
    ("AUS-008-DUPAS",      "Peter Norris Dupas",           "AUS", "", "serial", "stub"),
]

# ---------------------------------------------------------------------------
# QUARANTINE — excluded, with the reason. See docs/roster-audit.md.
# ---------------------------------------------------------------------------

QUARANTINE = [
    # (name as inherited, country as inherited, category, reason)
    ("Émile de Maupas", "Venezuela", "fabricated",
     "No such offender. Conflates Émile Maupas (French zoologist) and Charlemagne Émile de Maupas (French prefect of police). Appeared twice in the source list."),
    ("Félicien Tremblay", "Canada", "fabricated",
     "No such offender. Quebec's documented cases are Léopold Dion and William Fyfe, both already on the roster."),
    ("Michel Stocker", "Switzerland", "fabricated",
     "No such offender. Appears to be a corruption of Michel Peiry, now on the roster as CHE-001-PEIRY."),
    ("Jochum Sjöblom", "Finland", "fabricated",
     "No such offender. Finland's documented cases include Michael Penttilä, Ismo Junni, Reijo Hammar."),
    ("Elias Pical", "Philippines", "fabricated",
     "No such offender. Elias Pical is an Indonesian boxer, the country's first world champion."),
    ("Anwar Ali", "Bangladesh", "fabricated",
     "Not corroborated. No documented offender matching this name and description."),
    ("Ivan Podkopaev / 'Grand Gland Gang'", "Russia", "fabricated",
     "No such offender or group. The epithet matches no documented case."),
    ("Asisipho Mbekela", "South Africa", "defamation-risk",
     "PERMANENTLY EXCLUDED. Real living person convicted of falsifying academic qualifications. No connection to homicide. Must never be republished under any circumstances."),

    ("Sture Bergwall / 'Thomas Quick'", "Sweden", "exonerated",
     "All convictions overturned; fully exonerated. Moved to docs/investigative-failures.md as a false-confession case study. Must never appear in an offender roster."),
    ("Rex Heuermann", "USA", "sub-judice",
     "Proceedings ongoing, no conviction. Presumption of innocence applies. May be added as a stub with judicial_status='charged' only; no behavioural profile permitted."),

    ("Ted Kaczynski", "USA", "category-mismatch", "Ideological bombing campaign, not serial homicide."),
    ("Charles Manson", "USA", "category-mismatch", "Convicted under joint responsibility; did not personally commit the killings."),
    ("Bradley John Murdoch", "Australia", "category-mismatch", "Single murder."),
    ("Raymond John Denning", "Australia", "category-mismatch", "Prison escapee and armed robber. Not a killer."),
    ("Arthur Lucas", "Canada", "category-mismatch", "Single incident."),
    ("Luka Rocco Magnotta", "Canada", "category-mismatch", "Single murder."),
    ("Yuka Takaoka", "Japan", "category-mismatch", "Attempted murder, single victim. Living person; excluded."),
    ("Satoshi Uematsu", "Japan", "category-mismatch", "Mass murder, single event."),
    ("Woo Bum-kon", "South Korea", "category-mismatch", "Spree shooting, single event."),
    ("Mona Fandey", "Malaysia", "category-mismatch", "Single ritual murder."),
    ("Roch Thériault", "Canada", "category-mismatch", "Cult leader; one murder conviction."),
    ("Majid Kavousifard", "Iran", "category-mismatch", "Single political assassination."),
    ("Thug Behram", "India", "unreliable-record", "Semi-legendary 19th-century figure; attributed counts have no evidentiary basis."),

    ("Macario Alcalá Canchola", "Mexico", "needs-verification", "Not corroborated during audit."),
    ("Jeong Du-yeong", "South Korea", "needs-verification", "Possibly a corruption of Jeong Nam-gyu."),
    ("Jimmy Maketta", "South Africa", "needs-verification", "Not corroborated during audit."),
    ("Tsang Tsan-lam", "Hong Kong", "needs-verification", "Not corroborated during audit."),
    ("Giorgio William Vizzardelli", "Italy", "needs-verification", "Not corroborated during audit."),
    ("Marcelo Antelo", "Argentina", "needs-verification", "Not corroborated during audit."),

    ("Charles Sobhraj", "France", "needs-recoding", "Country of offences is wrong; offended across South and Southeast Asia. Requires a multi-jurisdiction record."),
    ("Pierre Chanal", "France", "needs-recoding", "Died before trial; never convicted. Requires the sub-judice/unadjudicated treatment."),
    ("Christopher Wilder", "Australia/USA", "duplicate-listing", "Retained once as USA-057-WILDER."),
]

# ---------------------------------------------------------------------------
# CASES — subjects excluded from the offender roster but documented in full
# under schema/case.schema.json. Never counted in offender aggregates.
# (id, name, iso3, case_type, status)
# ---------------------------------------------------------------------------

CASES = [
    ("USA-003-HALL",  "Larry DeWayne Hall",       "USA", "no_homicide_conviction", "in_progress"),
    ("USA-011-CORLL", "Dean Arnold Corll",        "USA", "died_before_trial", "in_progress"),
    ("USA-019-LAKE",  "Leonard Lake",             "USA", "died_before_trial", "stub"),
    ("USA-038-KEYES", "Israel Keyes",             "USA", "died_before_trial", "stub"),
    ("GBR-004-FWEST", "Frederick Walter Stephen West", "GBR", "died_before_trial", "stub"),
]

# ---------------------------------------------------------------------------
# UNSOLVED — cases, not offenders. These carry no behavioural profile.
# ---------------------------------------------------------------------------

UNSOLVED = [
    ("UNS-001-RIPPER",     "Whitechapel murders",          "GBR", "1888", "Offender never identified."),
    ("UNS-002-FIRENZE",    "Monster of Florence",          "ITA", "1968-1985", "Attributions contested; convictions disputed."),
    ("UNS-003-BRABANT",    "Brabant killers",              "BEL", "1982-1985", "Offenders never identified."),
    ("UNS-004-WESTMESA",   "West Mesa remains",            "USA", "2009", "Offender never identified."),
    ("UNS-005-ATLANTA",    "Atlanta child murders",        "USA", "1979-1981", "Wayne Williams convicted of two adult murders; the wider attribution is contested."),
]


def write(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)
    print(f"  {path.relative_to(ROOT)}: {len(rows)} rows")


def main():
    INDEX.mkdir(exist_ok=True)
    print("Building index files...")
    write(INDEX / "roster.csv",
          ["id", "name", "country_iso3", "epithet", "classification", "record_status"],
          ROSTER)
    write(INDEX / "cases.csv",
          ["id", "name", "country_iso3", "case_type", "record_status"],
          CASES)
    write(INDEX / "quarantine.csv",
          ["name_as_inherited", "country_as_inherited", "category", "reason"],
          QUARANTINE)
    write(INDEX / "unsolved-cases.csv",
          ["id", "case_name", "country_iso3", "period", "note"],
          UNSOLVED)

    allowed = {"serial", "healthcare", "poisoner"}
    bad = sorted({r[4] for r in ROSTER} - allowed)
    assert not bad, (
        f"disallowed classification(s): {bad}. There is no 'team' value: "
        "co-offenders each get their own record, linked by `co_offenders`. "
        "See docs/co-offenders.md.")

    ids = [r[0] for r in ROSTER]
    assert len(ids) == len(set(ids)), "duplicate ids in roster"
    names = [r[1] for r in ROSTER]
    assert len(names) == len(set(names)), "duplicate names in roster"
    case_ids = [r[0] for r in CASES]
    assert len(case_ids) == len(set(case_ids)), "duplicate ids in cases"
    overlap = set(ids) & set(case_ids)
    assert not overlap, f"id in both roster and cases: {overlap}"
    print(f"\nRoster: {len(ROSTER)} subjects. Cases: {len(CASES)}. "
          f"Quarantine: {len(QUARANTINE)}. Unsolved: {len(UNSOLVED)}.")
    print("No duplicate ids, and no id in both roster and cases.")


if __name__ == "__main__":
    main()
