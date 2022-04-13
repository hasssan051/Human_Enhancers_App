from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError,NumberRange, AnyOf


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
    chromStart = IntegerField('chromStart',validators=[DataRequired(),NumberRange(min=1,message='Please provide a number above 1')])
    chromEnd = IntegerField('chromEnd',validators=[DataRequired(),NumberRange(min=1,message='Please provide a number above 1'),validate_chromStart_chromEnd])
    system = SelectField('System',choices=['Any','Embryo','Musculoskeletal','Integumentary','Endocrine','Lymphatic','Urinary','Reproductive','Circulatory','Nervous','Digestive','Respiratory'])
    organ = SelectField('Organ', choices=['Any'])
    tissue = SelectField('Tissue',choices=['Any'])
    treated = BooleanField('Treated')
    disease = BooleanField('Disease')
    submit = SubmitField('Search')