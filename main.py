import fitz


def pdf_is_encrypted(file):
    pdf = fitz.Document(file)
    return pdf.isEncrypted


def encrypt_pdf_file(pdf, password, outfile, file):
    if not pdf_is_encrypted(file):
        perm = int(
            fitz.PDF_PERM_ACCESSIBILITY
            | fitz.PDF_PERM_PRINT
            | fitz.PDF_PERM_COPY
            | fitz.PDF_PERM_ANNOTATE
        )
        encrypt_meth = fitz.PDF_ENCRYPT_AES_256
        pdf.save(outfile, encryption=encrypt_meth, user_pw=password,
                 permissions=perm)
        if pdf.save:
            print("PDF encrypted")


def decrypt_pdf(file):
    if pdf_is_encrypted(file):
        password = input('Enter pdf password : ')
        pdf = fitz.open(file)
        if pdf.authenticate(password):
            pdf.save('decrypted.pdf')
            if pdf.save:
                print("PDF decrypted")
        else:
            print('Incorrect Password')


def main():
    file = 'protected.pdf'
    pdf = fitz.open(file)
    password = 'pass123'
    encrypt_pdf_file(pdf, password, 'protected.pdf', file)
    decrypt_pdf(pdf)


if __name__ == '__main__':
    main()
