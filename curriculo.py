from fpdf import FPDF
import os

class StyledCurriculumPDF(FPDF):
    def header(self):
        self.set_fill_color(128, 0, 0)  # Cor de fundo para o cabeçalho
        self.rect(0, 0, 210, 15, 'F')  # Retângulo para o topo
        self.ln(5)
        
    def add_photo(self, image_path):
        try:
            self.image(image_path, x=10, y=27, w=30)
        except:
            pass
        
    def user_info(self, name, location, phone, email, linkedin, github, photo_dir):
        whatsapp_link = "https://wa.me/+553..."  # Substitua pelo link do seu WhatsApp
        linkedin_link = "https://www.linkedin.com/"  # Substitua pelo seu perfil do LinkedIn
        github_link = "https://github.com/"  # Substitua pelo seu perfil do GitHub
        
        # Caminhos dos ícones
        whatsapp_icon = os.path.join(photo_dir, "whatsapp.png")
        linkedin_icon = os.path.join(photo_dir, "linkedin.png")
        github_icon = os.path.join(photo_dir, "github.png")

        #nome
        self.set_xy(45, 25)
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, name, ln=True)
        
        #localização
        self.set_xy(45, 35)
        self.set_font("Arial", "", 10)
        self.cell(90, 5, location, ln=True) # parametros: largura, altura, texto, quebra de linha
        
        #telefone e whatsapp
        self.set_xy(45, 40)
        self.cell(90, 5, phone, ln=True)
        self.image(whatsapp_icon, x=78, y=40, w=4)  # Ícone do WhatsApp
        self.link(78, 40, 4, 4, whatsapp_link)
        
        #email
        self.set_xy(45, 45)
        self.cell(90, 5, email, ln=True)
        
        #linkedin
        self.set_xy(45, 50)
        self.set_font("Arial", "I", 10)
        self.cell(90, 5, "LinkedIn: ", ln=False)
        self.image(linkedin_icon, x=61, y=51, w=3)  # Ícone do LinkedIn
        self.link(61, 51, 3, 3, linkedin_link)
        self.ln(5)
        
        #github
        self.set_xy(45, 55)
        self.cell(90, 5, "GitHub: alvarojpr", ln=False)
        self.image(github_icon, x=74, y=56, w=3)  # Ícone do GitHub
        self.link(74, 56, 3, 3, github_link)
        self.ln(5)
        
        
    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(128, 0, 0)
        self.cell(0, 10, title, ln=True)
        self.set_line_width(0.5)
        self.set_draw_color(128, 0, 0)
        self.line(self.get_x(), self.get_y(), 210 - self.get_x(), self.get_y())
        self.ln(5)
        
    def section_content(self, content):
        self.set_font("Arial", "", 11)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 8, content)
        self.ln(5)

def generate_curriculum(data):
    pdf = StyledCurriculumPDF()
    pdf.add_page()

    # Diretório onde as imagens estão localizadas
    photo_dir = os.path.join(os.getcwd(), "imagens")  # A pasta 'imagens' deve estar no mesmo diretório do script

    # Adicionando foto e informações do usuário
    if data.get("foto"):
        photo_path = os.path.join(photo_dir, "foto.png")  # Substitua pelo nome da foto se necessário
        pdf.add_photo(photo_path)

    pdf.user_info(data["nome"], data["localizacao"], data["telefone"], data["email"], data["linkedin"], data["github"], photo_dir)

    # Seções organizadas
    pdf.section_title("Resumo")
    pdf.section_content(data["resumo"])

    pdf.section_title("Habilidades e Competências")
    pdf.section_content(", ".join(data["habilidades"]))

    pdf.section_title("Experiência Profissional")
    pdf.section_content("\n".join(data["experiencia"]))

    pdf.section_title("Formação Acadêmica")
    pdf.section_content("\n".join(data["formacao"]))

    pdf.section_title("Idiomas")
    pdf.section_content(", ".join(data["idiomas"]))

    pdf.section_title("Hobbies")
    pdf.section_content(", ".join(data["hobbies"]))

    # Salvando o PDF
    pdf.output("curriculo.pdf")
    print("Currículo gerado com sucesso: curriculo.pdf")

# Dados para o currículo
dados = {
    "nome": "",
    "localizacao": "Cidade, Estado, País",
    "telefone": "(99) 99999-9999",
    "linkedin": "https://www.linkedin.com/in",
    "github": "https://github.com/",
    "email": "",
    "foto": "foto.png",  # Nome da foto, que deve estar no diretório de imagens
    "resumo": "Resumo sobre mim",
    "habilidades": ["", ""],
    "experiencia": ["Experiência 1", "Experiência 2"],
    "formacao": [""],
    "idiomas": ["Português (nativo)", "Inglês (avançado)"],
    "hobbies": ["Hobby 1", "Hobby 2"]
}

generate_curriculum(dados)
