from mcp.server.fastmcp import FastMCP

mcp = FastMCP("StocksMCPServer")


#마켓이 열려있는지 여부를 체크해주는 더미 함수
#리소스 추가
#리소스란 => 서버에서 데이터를 가져오는데 사용하는 GET 통신이랑 같은 개념
#동적 URL로 변경하고 싶을 경우 market://state/{symbol} 처럼 앞에 심볼 변수 추가
@mcp.resource("market://state")
def get_market_state() -> str:
    """Get the current market state

    Returns:
        str: The current market state
    """
    return "The market is open"


#주어진 주식 심볼과 수량에 따라 주식을 구매하는 기능
# tool은 POST같이 상태를 update, delete 하는 부분에서 비슷한 개념이다
@mcp.tool()
def buy_stock(symbol: str, quantity: int) -> str:
    """Buys a stock for a given symbol and quantity

    Args:
        symbol (str): The symbol of the company to buy stock for
        quantity (int): The quantity of stock to buy

    Returns:
        str: A string containing the result of the transaction
    """
    return f"Bought {quantity} shares of {symbol}"

#주식 심볼과 수량에 따라 주식을 판매하는 기능
@mcp.tool()
def sell_stock(symbol: str, quantity: int) -> str:
    """Sells a stock for a given symbol and quantity

    Args:
        symbol (str): The symbol of the company to sell stock for
        quantity (int): The quantity of stock to sell

    Returns:
        str: A string containing the result of the transaction
    """
    return f"Sold {quantity} shares of {symbol}"

#주어진 주식 심볼, 작년 수익, 회사 정보를 기반으로 주식 분석을 수행
#prompt 실행시 명령어 추가
@mcp.prompt()
def analyze_stock(symbol: str, last_years_profit: str, company_info: str) -> str:
    return f"""
    당신은 주식 분석가입니다. 주식 심볼이 주어졌고, 주식을 분석해야 합니다.
    다음은 수익 보고서입니다:
    {last_years_profit}
    다음은 회사 정보입니다:
    {company_info}
    다음은 심볼입니다:
    {symbol}
    수익 보고서와 회사 정보를 분석하여 주식에 대한 상세한 분석을 제공하세요.
    주식을 매수, 매도 또는 보유할지에 대한 추천을 하세요.
    """

if __name__ == "__main__":
    mcp.run()