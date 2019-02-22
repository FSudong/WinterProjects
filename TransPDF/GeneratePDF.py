import pdfkit

class Trans:

    def url2pdf(self,url,pdfname):

        pdfkit.from_url(url, pdfname)
        pass

    def html2pdf(self,html,pdfname):

        pdfkit.from_file(html, pdfname)
        pass

    def string2pdf(self,string,pdfname):
        pdfkit.from_string(string, pdfname)
        pass

if __name__ == '__main__':
    print("choose data type")
    t = Trans()
    # url网页生成
    t.url2pdf("http://baidu.com", "url_out.pdf")
    # html文件pdf
    t.html2pdf("te.html", "html_out.pdf")
    # 字符串变成pdf
    t.string2pdf("这就是一个pdf", "string_out.pdf")