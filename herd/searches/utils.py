from cmath import exp
from herd import db
from herd.models import experiments, merged_peak, mp_overlap_vista,vista,vista_in_mp,erna_in_mp,mp_overlap_erna,mp_narrow_accession

def return_search_result(chrom,chromStart,chromEnd,system=None,organ=None,tissue=None,treated=False,disease=False):
    result = []
    if system == 'All':
        result = db.session.query(merged_peak).with_entities(merged_peak.herdAccessionNum,merged_peak.chrom,merged_peak.chromStart,merged_peak.chromEnd,
        merged_peak.Prefixes, mp_overlap_vista.vistaId, vista_in_mp.vistaId,mp_overlap_erna.ernaId,erna_in_mp.ernaId
        ).filter((merged_peak.chrom == chrom) & (merged_peak.chromStart >= chromStart) & (merged_peak.chromEnd <= chromEnd)
        ).outerjoin(vista_in_mp
        ).outerjoin(mp_overlap_vista
        ).outerjoin(erna_in_mp
        ).outerjoin(mp_overlap_erna
        ).all()
        return result
    else:
        if organ == 'All':
            

            #db.session.query().filter((merged_peak.chrom== chrom) & (merged_peak.chromStart>= chromStart) & (merged_peak.chromEnd<= chromEnd)).join()
            first_sub = merged_peak.query.filter((merged_peak.chrom== chrom) & (merged_peak.chromStart>= chromStart) & (merged_peak.chromEnd<= chromEnd)).subquery()
            second_sub = mp_narrow_accession.query.join(experiments, mp_narrow_accession.narrowPeaksAccession== experiments.narrowPeaksAccession
            ).filter(experiments.system == system).subquery()
            print(db.session.query(first_sub.mergedPeakId).join(second_sub, first_sub.mergedPeakId==second_sub.mergedPeakId).all())
            return []

            print(2)
            subquery = db.session.query(mp_narrow_accession.mergedPeakId
            ).outerjoin(experiments,mp_narrow_accession.narrowPeaksAccession == experiments.narrowPeaksAccession
            ).filter(experiments.system == system).subquery()
        else:
            if tissue == 'All':
                print(3)
                subquery = db.session.query(mp_narrow_accession.mergedPeakId
                ).outerjoin(experiments,mp_narrow_accession.narrowPeaksAccession == experiments.narrowPeaksAccession
                ).filter((experiments.system == system) & (experiments.organ == organ)).subquery()
               
            else:
                if not treated and not disease:
                    subquery = db.session.query(mp_narrow_accession.mergedPeakId
                    ).outerjoin(experiments,mp_narrow_accession.narrowPeaksAccession == experiments.narrowPeaksAccession
                    ).filter((experiments.system == system) & (experiments.organ == organ) & (experiments.tissue == tissue)).subquery()
                elif treated and not disease:
                    subquery = db.session.query(mp_narrow_accession.mergedPeakId
                    ).outerjoin(experiments,mp_narrow_accession.narrowPeaksAccession == experiments.narrowPeaksAccession
                    ).filter((experiments.system == system) & (experiments.organ == organ) & (experiments.tissue == tissue) & (experiments.treated == 1)).subquery()
                elif disease and not treated:
                    subquery = db.session.query(mp_narrow_accession.mergedPeakId
                    ).outerjoin(experiments,mp_narrow_accession.narrowPeaksAccession == experiments.narrowPeaksAccession
                    ).filter((experiments.system == system) & (experiments.organ == organ) & (experiments.tissue == tissue) & (experiments.diseased == 1)).subquery()
                else:
                    subquery = db.session.query(mp_narrow_accession.mergedPeakId
                    ).outerjoin(experiments,mp_narrow_accession.narrowPeaksAccession == experiments.narrowPeaksAccession
                    ).filter((experiments.system == system) & (experiments.organ == organ) & (experiments.tissue == tissue) & (experiments.treated == 1) &
                    (experiments.diseased == 1)).subquery()


    result = db.session.query(merged_peak).with_entities(merged_peak.herdAccessionNum,merged_peak.chrom,merged_peak.chromStart,merged_peak.chromEnd,
    merged_peak.Prefixes,mp_overlap_vista.vistaId, vista_in_mp.vistaId,mp_overlap_erna.ernaId,erna_in_mp.ernaId
    ).filter((merged_peak.chrom == chrom) & (merged_peak.chromStart >= chromStart) & (merged_peak.chromEnd <= chromEnd)
    ).outerjoin(vista_in_mp
    ).outerjoin(mp_overlap_vista
    ).outerjoin(erna_in_mp
    ).outerjoin(mp_overlap_erna
    ).filter(merged_peak.mergedPeakId.in_(subquery)).all()

    return result


def return_if_result_zero(chrom,chromStart,chromEnd):
    result = []
    query_1 = db.session.query(merged_peak).with_entities(merged_peak.herdAccessionNum,merged_peak.chrom,merged_peak.chromStart,merged_peak.chromEnd,
    merged_peak.Prefixes, mp_overlap_vista.vistaId, vista_in_mp.vistaId,mp_overlap_erna.ernaId,erna_in_mp.ernaId
    ).filter((merged_peak.chrom == chrom) & (merged_peak.chromStart <= chromStart)
    ).outerjoin(vista_in_mp
    ).outerjoin(mp_overlap_vista
    ).outerjoin(erna_in_mp
    ).outerjoin(mp_overlap_erna
    ).first()
    
    query_2 = result.append(db.session.query(merged_peak).with_entities(merged_peak.herdAccessionNum,merged_peak.chrom,merged_peak.chromStart,merged_peak.chromEnd,
        merged_peak.Prefixes, mp_overlap_vista.vistaId, vista_in_mp.vistaId,mp_overlap_erna.ernaId,erna_in_mp.ernaId
        ).filter((merged_peak.chrom == chrom) & (merged_peak.chromEnd >= chromEnd)
        ).outerjoin(vista_in_mp
        ).outerjoin(mp_overlap_vista
        ).outerjoin(erna_in_mp
        ).outerjoin(mp_overlap_erna
        ).first())
    if query_1 and query_2:
        result.append(query_1)
        result.append(query_2)
    elif query_1:
        result.append(query_1)
    elif query_2:
        result.append(query_2)
    
    return result