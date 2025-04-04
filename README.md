# mcpTutorial

가상의 **mcp 서버**를 구축하여 트레이더가 주식을 매수, 매도하고 **cursor AI** 채팅창에서 데이터를 조회하는 **Python SDK**

## 기능

- **마켓 상태 확인**: 마켓이 열려 있는지 여부를 체크하는 기능
- **주식 매수**: 주어진 주식 심볼과 수량에 따라 주식을 구매
- **주식 매도**: 주식 심볼과 수량에 따라 주식을 판매
- **주식 분석**: 주어진 주식 심볼, 작년 수익, 회사 정보를 기반으로 주식 분석 수행

## 사용 방법

1. **서버 시작**: `mcp.run()`을 호출하여 서버를 시작합니다.
2. **리소스 및 툴 사용**: `@mcp.resource`와 `@mcp.tool` 데코레이터를 사용하여 리소스와 툴을 정의합니다.
3. **프롬프트 사용**: `@mcp.prompt` 데코레이터를 사용하여 주식 분석을 수행합니다.
