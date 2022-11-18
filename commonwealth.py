import sys
import requests
import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
loggerFileHandler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024*1024,
    backupCount=1,
    encoding="utf-8",
)
fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
loggerFileHandler.setFormatter(fmt)
logger.addHandler(loggerFileHandler)

def getUnits() -> str:
    url = "https://www.commonwealthlanding.com/CmsSiteManager/callback.aspx?act=Proxy/GetUnits&available=true&honordisplayorder=true&siteid=4460382&leaseterm=12&dateneeded=2023-01-03&callback=jQuery224007571119365756718_1668786545046&_=1668786545050"
    headers = {
        "authority": "www.commonwealthlanding.com",
        "method": "GET",
        "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "referer": "https://www.commonwealthlanding.com/",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.request("GET", url, headers=headers)
        resp.raise_for_status()
    except:
        raise Exception(f"Error getUnits(): {resp.status_code}: {resp.reason}")
    return resp.text

def parseUnits(units: str) -> str:
    """
    Get only the JSON part of the response as a string
    """
    start = units.find("{")
    end = units.rfind("}")
    if start == -1 or end == -1:
        raise Exception("Error parseUnits(): No JSON found")
    units = units[start:end+1]
    return units

def main():
    units = ""
    try:
        units = getUnits()
    except Exception as e:
        logger.error(e)
        sys.exit(1)

    try:
        units = parseUnits(units)
    except Exception as e:
        logger.error(e)
        sys.exit(1)
    logger.info(units)

if __name__ == "__main__":
    main()