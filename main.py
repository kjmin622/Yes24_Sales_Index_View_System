import crawling
import email_handle


def main():
    datas = crawling.sales_index_crawling(crawling.get_name_address_list())
    datas = sorted(datas, key=lambda x: x[2], reverse=True)
    html_content = """
    <html>
        <body>
            <table style="border-collapse: collapse; width: 100%;">
                <tr>
                    <th>번호</th>
                    <th style="border: 1px solid #ddd; background-color: #4CAF50; color: white; padding: 8px;">책 이름</th>
                    <th style="border: 1px solid #ddd; background-color: #4CAF50; color: white; padding: 8px;">판매지수</th>
                </tr>
    """

    for idx, (title, link, sales_index) in enumerate(datas, start=1):
        html_content += f"""
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">{idx}</td>
                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;"><a href='{link}'>{title}</a></td>
                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">{sales_index}</td>
                </tr>
    """

    html_content += """
            </table>
        </body>
    </html>
    """

    email_handle.email_send(html_content)


main()
