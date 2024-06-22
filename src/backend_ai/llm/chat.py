import boto3
import sys
from langchain_community.llms.bedrock import Bedrock
from langchain.chat_models import BedrockChat
from langchain import PromptTemplate
from langchain import LLMChain


async def chat(query):
    llm = Bedrock(
        model_id="anthropic.claude-instant-v1",
        region_name="us-west-2",
    )

    template = """
あなたは優秀な会社員です。議論の論点を正確に理解し、わかりやすく回答することができます。
末尾の会議内容を、以下のテンプレートでまとめてください。該当する項目が存在しない場合は「不明」と記載してください。会議で言及されていないことをまとめに載せないでください。
打ち合わせ情報: 打ち合わせの基本的な情報を提供します。これには以下の項目が含まれます。
- 日時: timelineのうち，最も早い日時を記載してください。(日時は「YYYY/MM/DD HH:MM」の形式で記載してください)
- 話されたテーマ一覧（それぞれ一行で簡潔に）
    topics:
- 出席者リスト（名前のみ）
    attendees:
- 議事録作成者（今回は「議事録AI」と書いてください）
議論の内容: 打ち合わせ中の議論の要約を記載します。意思決定に至るまでのプロセスや、異なる意見や提案内容も記載します。箇条書きで記載してください．トピックの順番は話された順番に従ってください。トピックの末尾には、そのトピックでの意見の最初の主張者を記載してください．


----

timeline:
{source_knowledge}
"""
    prompt = PromptTemplate(template=template, input_variables=["source_knowledge"])
    chain = LLMChain(
        prompt=prompt,
        llm=llm,
    )
    return chain.run(
        {
            "source_knowledge": query,
        }
    )
