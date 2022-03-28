from flask import Flask
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,NumberRange, AnyOf
from herd.models import User


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[
                            DataRequired(), Length(min=2, max=26)])
    lastname = StringField('Last Name', validators=[
                           DataRequired(), Length(min=2, max=26)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), Length(min=8), EqualTo('password')])
    occupation = SelectField('Occupation', choices=[
                             'Student', 'Researcher', 'Random Dude', 'With an Organization', 'Explorer'])
    submit = SubmitField('Sign Up')

    # function to check whether email already exists in db
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is already taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8)])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Log in')


class UpdateAccountForm(FlaskForm):
    firstname = StringField('First Name', validators=[
                            DataRequired(), Length(min=2, max=26)])
    lastname = StringField('Last Name', validators=[
                           DataRequired(), Length(min=2, max=26)])
    email = StringField('Email')
    occupation = SelectField('Occupation', choices=[
                             'Student', 'Researcher', 'Self-Employed', 'With an Organization', 'Explorer'])
    submit = SubmitField('Update')


def validate_chromStart_chromEnd(form,chromEnd):
    if chromEnd.data<= form.chromStart.data:
        raise ValidationError('chromEnd must be larger than chromStart')

def validate_chromosome(form,chromosome):
    if chromosome.data == 'None':
        raise ValidationError('Please select a chromosome value')

class QueryForm(FlaskForm):
    chromosome = SelectField('Chromosome', choices=['None','chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10',
                             'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY'], validators=[AnyOf(['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10',
                             'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY'],'Please select a chromosome value')])
    chromStart = IntegerField('chromStart',validators=[DataRequired(),NumberRange(min=1,max=500000,message='Please provide number between 1 and 500000')])
    chromEnd = IntegerField('chromEnd',validators=[DataRequired(),NumberRange(min=1,max=500000,message='Please provide number between 1 and 500000'),validate_chromStart_chromEnd])
    tissue = SelectField('Tissue',choices=['None','Heart', 'Cell Line', 'Pancreas', 'Liver', 'Bone Marrow', 'Ovary',
       'Lymph', 'Brain', 'Embryo', 'Muscle', 'Artery', 'Vein', 'Lung',
       'Ligament', 'Adrenal', 'Placenta', 'Lymphatic vessel', 'Colon',
       'Eye', 'Blood vessel', 'Kidney', 'iPSC', 'Skin', 'Epidermis',
       'Spleen', 'Mouth', 'Prostate ', 'Peripheral Nerve', 'Esophagus',
       'Small Intestine', 'Bone ', 'Testis', 'Thyroid', 'Uterus',
       'Gallbladder', 'Abdomen', 'Breast', 'Thymus', 'Germinal Center',
       'Stomach', 'Vagina', 'Ureter'])
    organ = SelectField('Organ', choices=['None','Ventricle (Right)', 'T cell acute lymphoblastic leukemia',
       'Ventricle (Left)', 'Pancreas', 'Liver (Right Lobe)',
       'B cell multiple myeloma', 'Hematopoietic progenitor cell',
       'Ovary', 'Chronic myeloid leukemia', 'T cell effector memory',
       'T cell', 'T cell regulatory', 'Middle frontal area 46',
       'Posterior cingulate gyrus', 'Head of caudate nucleus', 'Forelimb',
       'Hindlimb', 'Acute myeloid leukemia ', 'Breast adenocarcinoma',
       'Psoas muscle', 'Frontal cortex', 'Colon adenocarcinoma', 'Aorta',
       'Cardiac myoblast (differentiated from H7 hESC)',
       'T cell helper type 2', 'Endoderm', 'T cell helper type 9',
       'T cell helper type 1', 'Breast epithelium', 'Heart',
       'Umbilical venous endothelium ', 'Embryonic stem cell',
       'Lung (Left)', 'Peridontal ligament fibroblast',
       'B cell lymphoblastoid', 'Lung (Left, upper lobe)',
       'Adrenal gland', 'Cardiac muscle (differentiated from RUES2 hESC)',
       'Cerebellum', 'Chronic myeloid leukemia ',
       'Prostate adenocarcinoma', 'Kidney', 'Medulla oblongata',
       'Middle frontal gyrus', 'Placenta',
       'Dermis lymphatic microvascular endothelium',
       'Acute megakaryocytic leukemia', 'Astrocyte', 'B cell ',
       'Colon (Left)', 'Gastrocnemius medialis',
       'Hepatocyte (differentiated from H9 hESC)', 'T cell memory',
       'Hindlimb (Left)', 'Liver hepatocellular carcinoma', 'Skin ',
       'Cervical adenocarcinoma', 'Conjunctival fibroblast',
       'Microvascular endothelium (Lung)', 'Myoblast',
       'Breast ductal carcinoma', 'Monocyte', 'Lung carcinoma',
       'Glomerular endothelium', 'Neuroblastoma', 'Retinoblastoma',
       'Dermis blood vessel endothelium', 'Chorion', 'Forelimb (Left)',
       'Pericyte', 'Acute myeloid leukemia',
       'Myocardium inferior (Left Ventricle)', 'Cardiac fibroblast',
       'Skin fibroblast', 'Nephron progenitor cell',
       'iPSC (induced pluripotent stem cell)', 'Renal carcinoma cell',
       'Stromal cell', 'Bronchial epithelium', 'Foreskin fibroblast',
       'Endometrial adenocarcinoma', 'Hepatocyte', 'Kidney tubule cell',
       'Melanocyte', 'Testicular embryonal carcinoma cell',
       'Glomerular epithelium', 'Facial prominence', 'Lung fibroblast',
       'T cell central memory', 'Epicardial mesothelium', 'Brain',
       'Renal cell carcinoma (clear cell)', 'Lung',
       "B cell (Burkitt's lymphoma)", 'T cell central memory ',
       'Occipital lobe', 'Superior temporal gyrus',
       'T cell naive resting', 'T cell helper 17', 'Urothelium', 'Spleen',
       'Neural crest', 'Lung (Left, lower lobe)',
       'Cerebellum, posterior fossa, medulloblastoma', 'Osteosarcoma',
       'Aorta (Thoracic)', "Hippocampus Ammon's horn", 'Limb', 'Retina',
       'Tongue', 'Urinary bladder', 'Iris pigment epithelial cell',
       'Gingiva fibroblast', 'Dendritic cell', 'Colon epithelium', 'Eye',
       'Lung mesothelioma (NSCLC)', 'Umbilical cord',
       'Astrocyte (cerebellum)', 'Astrocyte (hippocampus)',
       'Prostate epithelium', 'Trophoblast', 'Choroid plexus epithelium',
       'Inferior vena cava', 'Pancreas adenocarcinoma', 'Sciatic nerve',
       'Pulmonary artery endothelium', 'Macrophage (Inflammatory)',
       'Tibial nerve', 'Squamous epithelium', 'Cardiac septum',
       'B cell naive', 'Myocardium superior (Left Ventricle) ',
       'Pancreas ductal carcinoma', 'Neural progenitor cell', 'Midbrain',
       'Cardiovascular progenitor cell (differentiated from H7 hESC)',
       'Stromal cell (bone marrow)', "Peyer's patch",
       'Amniotic epithelium', 'Epithelium', 'Colon (Transverse)',
       'Cardiac muscle', 'Non-pigmented ciliary epithelial cell',
       'Osteoblast', 'Retinal pigment epithelial cell', 'Testis', 'Liver',
       'Thyroid', 'Colon (descending) mucosa',
       'Smooth muscle cell (brain vasculature)', 'Pancreas (Body)',
       'Colon (Sigmoid)', 'Uterus', 'Gallbladder mucosa', 'Prostate',
       'Artery (Tibia)', 'Aorta (Ascending)', 'Cerebellar cortex', 'Pons',
       'Glioblastoma', 'Omental fat pad', 'Olfactory neurosphere',
       'Globus pallidus', 'Amniotic stem cell',
       'Pulmonary artery fibroblast',
       'Ecto neural progenitor cell (differentiated from H9 hESC)',
       'Rhabdomyosarcoma', 'Astrocyte (spinal cord)', 'Keratinocyte',
       'Breast fibroblast', 'Astrocytoma', 'Caudate nucleus',
       'Microvascular endothelium (Brain)',
       "Rhabdoid tumor (Wilm's tumor, Kidney)",
       'Acute promyelocytic leukemia',
       'Activated CD4-positive, alpha-beta T cell', 'Activated T-cell',
       'Activated CD8-positive, alpha-beta memory T cell', 'T-cell',
       'Spinal cord', 'Pancreas epithelium', 'Stomach',
       'B cell (non-Hodgkin lymphoma)', 'Cerebellum medulloblastoma',
       'T cell effector', 'T cell naïve',
       'Myocyte (differentiated from LHCN-M2)', 'Colon carcinoma',
       'Kidney (Left)', 'T cell helper 17 ', 'Myotube', 'Skeletal muscle',
       'Fibroblast (Aortic adventitia)', 'Atrium (Right)', 'T cell naive',
       'Kidney (Right)', 'B lymphoblast (Multiple myeloma)',
       'Muscle (Ewing sarcoma)',
       'Bipolar neuron (differentiated from GM23338 iPSC)',
       'Glomerular visceral epithelial cell', 'Lung adenocarcinoma',
       'Proximal tubular cell',
       'Mesodermal cell (differentiated from H7 hESC)', 'Putamen',
       'B cell', 'Fibrosarcoma', 'Chronic myeloid leukemia (in G1 phase)',
       'Villous mesenchyme fibroblast', 'Dermal fibroblast',
       'Kidney epithelium', 'Colon mucosa', 'Renal cortical epithelium',
       'Hepatic stellate cell', 'Progenitor cell of endocrine pancreas',
       'Renal adenocarcinoma', 'Kidney capillary endothelium',
       'Parietal cortex (Inferior)', 'Skin fibroblast (abdomen)',
       'T cell follicular helper',
       'Chronic myeloid leukemia (in G2 phase)', 'Gingival fibroblast',
       'Melanoma', 'Adipocyte', 'Germinal center tissue',
       'T cell helper 22 ', 'Proximal tubule epithelium', 'Femur',
       'Islet precursor cell', 'Coronary artery',
       'Macrophage (Suppressor)', 'Myocardium inferior (Right Ventricle)',
       'Vagina', 'Suprapubic skin', 'Muscularis mucosa',
       'Heart Ventricle (Left)', 'Skin (Lower leg)', 'Liver (Left Lobe)',
       'Atrium (Left cardiac)', 'Renal adenocarcinoma (clear cell)',
       'Heart Ventricle (Right)', 'Ureter', 'Atrium (Left)',
       'Myocardium superior (Right Ventricle) ', 'Mesenteric fat pad',
       'Lung (Right, lower lobe)', 'Atrium (Right, auricular region)',
       'Mesenchymal stem cell (dedifferentiated)',
       'Lung (Right, upper lobe)', 'Endothelium', 'Natural killer cell',
       'Brain organoid'])
    treated = BooleanField('Treated')
    disease = BooleanField('Disease')

    submit = SubmitField('Search')

    