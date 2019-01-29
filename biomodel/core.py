""" Class model autogenerated from flask model """

class SearchResult():
    """
    SearchResult

    Arguments
    ---------
     numFound : 

         total number of associations matching query

     start : 

         Cursor position

     facet_counts : 

         Mapping between field names and association counts

     facet_pivot : 

         Populated in facet_pivots is passed

    """
    def __init__(self,
                 id=None,
                 numFound=None,
                 start=None,
                 facet_counts=None,
                 facet_pivot=None,
                 **kwargs):
        self.id=id
        self.numFound=numFound
        self.start=start
        self.facet_counts=facet_counts
        self.facet_pivot=facet_pivot


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = SearchResult()
        if 'facet_pivot' in json_obj:
            obj.facet_pivot = json_obj['facet_pivot']
        if 'start' in json_obj:
            obj.start = json_obj['start']
        if 'facet_counts' in json_obj:
            obj.facet_counts = json_obj['facet_counts']
        if 'numFound' in json_obj:
            obj.numFound = json_obj['numFound']
        return obj

class AbstractPropertyValue():
    """
    AbstractPropertyValue

    Arguments
    ---------
     val : 

         value part

     pred : 

         predicate (attribute) part

     xrefs : 

         Xrefs provenance for property-value

    """
    def __init__(self,
                 id=None,
                 val=None,
                 pred=None,
                 xrefs=None,
                 **kwargs):
        self.id=id
        self.val=val
        self.pred=pred
        self.xrefs=xrefs


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = AbstractPropertyValue()
        if 'pred' in json_obj:
            obj.pred = json_obj['pred']
        if 'xrefs' in json_obj:
            obj.xrefs = [x for x in json_obj['xrefs']]
        if 'val' in json_obj:
            obj.val = json_obj['val']
        return obj

class SynonymPropertyValue(AbstractPropertyValue):
    """
    SynonymPropertyValue

    Superclass: AbstractPropertyValue

    Arguments
    ---------
    """
    def __init__(self,
                 id=None,
                 **kwargs):
        super(SynonymPropertyValue, self).__init__(id, **kwargs)


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = SynonymPropertyValue()
        if 'pred' in json_obj:
            obj.pred = json_obj['pred']
        if 'xrefs' in json_obj:
            obj.xrefs = [x for x in json_obj['xrefs']]
        if 'val' in json_obj:
            obj.val = json_obj['val']
        return obj

class AssociationPropertyValue(AbstractPropertyValue):
    """
    AssociationPropertyValue

    Superclass: AbstractPropertyValue

    Arguments
    ---------
    """
    def __init__(self,
                 id=None,
                 **kwargs):
        super(AssociationPropertyValue, self).__init__(id, **kwargs)


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = AssociationPropertyValue()
        if 'pred' in json_obj:
            obj.pred = json_obj['pred']
        if 'xrefs' in json_obj:
            obj.xrefs = [x for x in json_obj['xrefs']]
        if 'val' in json_obj:
            obj.val = json_obj['val']
        return obj

class Node():
    """
    Node

    Arguments
    ---------
     id : 

         ID or CURIE

     lbl : 

         human readable label, maps to rdfs:label

    """
    def __init__(self,
                 id=None,
                 lbl=None,
                 **kwargs):
        self.id=id
        self.lbl=lbl


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Node()
        if 'lbl' in json_obj:
            obj.lbl = json_obj['lbl']
        if 'id' in json_obj:
            obj.id = json_obj['id']
        return obj

class Edge():
    """
    Edge

    Arguments
    ---------
     sub : 

         Subject (source) Node ID

     pred : 

         Predicate (relation) ID

     obj : 

         Object (target) Node ID

    """
    def __init__(self,
                 id=None,
                 sub=None,
                 pred=None,
                 obj=None,
                 **kwargs):
        self.id=id
        self.sub=sub
        self.pred=pred
        self.obj=obj


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Edge()
        if 'pred' in json_obj:
            obj.pred = json_obj['pred']
        if 'obj' in json_obj:
            obj.obj = json_obj['obj']
        if 'sub' in json_obj:
            obj.sub = json_obj['sub']
        return obj

class Graph():
    """
    Graph

    Arguments
    ---------
     nodes : 

         All nodes in graph

     edges : 

         All edges in graph

    """
    def __init__(self,
                 id=None,
                 nodes=None,
                 edges=None,
                 **kwargs):
        self.id=id
        self.nodes=nodes
        self.edges=edges


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Graph()
        if 'nodes' in json_obj:
            obj.nodes = [Node.from_json(x) for x in json_obj['nodes']]
        if 'edges' in json_obj:
            obj.edges = [Edge.from_json(x) for x in json_obj['edges']]
        return obj

class NamedObject():
    """
    NamedObject

    Arguments
    ---------
     id : 

         ID or CURIE e.g. MGI:1201606

     label : 

         RDFS Label

     categories : 

         Type of object

     description :

         Description (or definition) of an object

     synonyms : 

         list of synonyms or alternate labels

    """
    def __init__(self,
                 id=None,
                 label=None,
                 categories=None,
                 synonyms=None,
                 description=None,
                 **kwargs):
        self.id=id
        self.label=label
        self.categories=categories
        self.synonyms=synonyms
        self.description=description


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = NamedObject()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        return obj

class Relation(NamedObject):
    """
    Relation

    Superclass: NamedObject

    Arguments
    ---------
    """
    def __init__(self,
                 id=None,
                 **kwargs):
        super(Relation, self).__init__(id, **kwargs)


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Relation()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        return obj

class Publication(NamedObject):
    """
    Publication

    Superclass: NamedObject

    Arguments
    ---------
    """
    def __init__(self,
                 id=None,
                 **kwargs):
        super(Publication, self).__init__(id, **kwargs)


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Publication()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        return obj

class Taxon():
    """
    Taxon

    Arguments
    ---------
     id : 

         CURIE ID, e.g. NCBITaxon:9606

     label : 

         RDFS Label

    """
    def __init__(self,
                 id=None,
                 label=None,
                 **kwargs):
        self.id=id
        self.label=label


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Taxon()
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'id' in json_obj:
            obj.id = json_obj['id']
        return obj

class BioObject(NamedObject):
    """
    BioObject

    Superclass: NamedObject

    Arguments
    ---------
     taxon : 

         Taxon to which the object belongs

    """
    def __init__(self,
                 id=None,
                 taxon=None,
                 inheritance=None,
                 clinical_modifiers=None,
                 association_counts=None,
                 **kwargs):
        super(BioObject, self).__init__(id, **kwargs)
        self.taxon = taxon
        self.inheritance = inheritance
        self.clinical_modifiers = clinical_modifiers
        self.association_counts = association_counts


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = BioObject()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        if 'taxon' in json_obj:
            obj.taxon = Taxon.from_json(json_obj['taxon'])
        if 'description' in json_obj:
            obj.description = json_obj['description']
        if 'inheritance' in json_obj:
            obj.inheritance = json_obj['inheritance']
        if 'clinical_modifiers' in json_obj:
            obj.clinical_modifiers = json_obj['clinical_modifiers']
        if 'association_counts' in json_obj:
            obj.association_counts = json_obj['association_counts']
        return obj

class AnnotationExtension():
    """
    AnnotationExtension

    Arguments
    ---------
     relation_chain : 

         Relationship type. If more than one value, interpreted as chain

     filler : 

         Extension interpreted as OWL expression (r1 some r2 some .. some filler).

    """
    def __init__(self,
                 id=None,
                 relation_chain=None,
                 filler=None,
                 **kwargs):
        self.id=id
        self.relation_chain=relation_chain
        self.filler=filler


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = AnnotationExtension()
        if 'filler' in json_obj:
            obj.filler = NamedObject.from_json(json_obj['filler'])
        if 'relation_chain' in json_obj:
            obj.relation_chain = [Relation.from_json(x) for x in json_obj['relation_chain']]
        return obj

class Association():
    """
    Association

    Arguments
    ---------
     id : 

         Association/annotation unique ID

     type : 

         Type of association, e.g. gene-phenotype

     subject : 

         Subject of association (what it is about), e.g. ClinVar:nnn, MGI:1201606

     subject_extension : 

         Additional properties of the subject in the context of this association.

     object : 

         Object (sensu RDF), aka target, e.g. HP:0000448, MP:0002109, DOID:14330

     object_extension : 

         Additional properties of the object in the context of this association

     relation : 

         Relationship type connecting subject and object

     qualifiers : 

         Qualifier on the association

     evidence_graph : 

         An indirect association is a join between two or more direct assocations, e.g. gene to disease via ortholog. We record the full set of associations as a graph object

     evidence_types : 

         Evidence types (ECO classes) extracted from evidence graph

     provided_by : 

         Provider of association, e.g. Orphanet, ClinVar

     publications : 

         Publications supporting association, extracted from evidence graph

    """
    def __init__(self,
                 id=None,
                 type=None,
                 subject=None,
                 subject_extension=None,
                 object=None,
                 object_extension=None,
                 relation=None,
                 qualifiers=None,
                 evidence_graph=None,
                 evidence_types=None,
                 provided_by=None,
                 publications=None,
                 **kwargs):
        self.id=id
        self.type=type
        self.subject=subject
        self.subject_extension=subject_extension
        self.object=object
        self.object_extension=object_extension
        self.relation=relation
        self.qualifiers=qualifiers
        self.evidence_graph=evidence_graph
        self.evidence_types=evidence_types
        self.provided_by=provided_by
        self.publications=publications


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Association()
        if 'publications' in json_obj:
            obj.publications = [Publication.from_json(x) for x in json_obj['publications']]
        if 'subject_extension' in json_obj:
            obj.subject_extension = [AnnotationExtension.from_json(x) for x in json_obj['subject_extension']]
        if 'type' in json_obj:
            obj.type = json_obj['type']
        if 'relation' in json_obj:
            obj.relation = Relation.from_json(json_obj['relation'])
        if 'evidence_types' in json_obj:
            obj.evidence_types = [NamedObject.from_json(x) for x in json_obj['evidence_types']]
        if 'object' in json_obj:
            obj.object = BioObject.from_json(json_obj['object'])
        if 'object_extension' in json_obj:
            obj.object_extension = [AnnotationExtension.from_json(x) for x in json_obj['object_extension']]
        if 'subject' in json_obj:
            obj.subject = BioObject.from_json(json_obj['subject'])
        if 'provided_by' in json_obj:
            obj.provided_by = [x for x in json_obj['provided_by']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'evidence_graph' in json_obj:
            obj.evidence_graph = Graph.from_json(json_obj['evidence_graph'])
        if 'qualifiers' in json_obj:
            obj.qualifiers = [AssociationPropertyValue.from_json(x) for x in json_obj['qualifiers']]
        return obj

class ChainedAssociation():
    """
    ChainedAssociation

    Arguments
    ---------
     proximal_association : 

         immediate association, between subject and intermediate object

     distal_associations : 

         Associations where the intermediate object is the subject

    """
    def __init__(self,
                 id=None,
                 proximal_association=None,
                 distal_associations=None,
                 **kwargs):
        self.id=id
        self.proximal_association=proximal_association
        self.distal_associations=distal_associations


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = ChainedAssociation()
        if 'proximal_association' in json_obj:
            obj.proximal_association = Association.from_json(json_obj['proximal_association'])
        if 'distal_associations' in json_obj:
            obj.distal_associations = [Association.from_json(x) for x in json_obj['distal_associations']]
        return obj

class CompactAssociationSet():
    """
    CompactAssociationSet

    Arguments
    ---------
     subject : 

         Subject of association (what it is about), e.g. MGI:1201606

     relation : 

         Relationship type connecting subject and object list

     objects : 

         List of O, for a given (S,R) pair, yielding (S,R,O) triples. E.g. list of MPs for (MGI:nnn, has_phenotype)

    """
    def __init__(self,
                 id=None,
                 subject=None,
                 relation=None,
                 objects=None,
                 **kwargs):
        self.id=id
        self.subject=subject
        self.relation=relation
        self.objects=objects


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = CompactAssociationSet()
        if 'objects' in json_obj:
            obj.objects = [x for x in json_obj['objects']]
        if 'subject' in json_obj:
            obj.subject = json_obj['subject']
        if 'relation' in json_obj:
            obj.relation = json_obj['relation']
        return obj

class AssociationResults(SearchResult):
    """
    AssociationResults

    Superclass: SearchResult

    Arguments
    ---------
     associations : 

         Complete representation of full association object, plus evidence

     compact_associations : 

         Compact representation in which objects (e.g. phenotypes) are collected for subject-predicate pairs

     objects : 

         List of distinct objects used

    """
    def __init__(self,
                 id=None,
                 associations=None,
                 compact_associations=None,
                 objects=None,
                 **kwargs):
        super(AssociationResults, self).__init__(id, **kwargs)
        self.associations=associations
        self.compact_associations=compact_associations
        self.objects=objects


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = AssociationResults()
        if 'facet_pivot' in json_obj:
            obj.facet_pivot = json_obj['facet_pivot']
        if 'start' in json_obj:
            obj.start = json_obj['start']
        if 'facet_counts' in json_obj:
            obj.facet_counts = json_obj['facet_counts']
        if 'numFound' in json_obj:
            obj.numFound = json_obj['numFound']
        if 'objects' in json_obj:
            obj.objects = [x for x in json_obj['objects']]
        if 'compact_associations' in json_obj:
            obj.compact_associations = [CompactAssociationSet.from_json(x) for x in json_obj['compact_associations']]
        if 'associations' in json_obj:
            obj.associations = [Association.from_json(x) for x in json_obj['associations']]
        return obj

class SequencePosition():
    """
    SequencePosition

    Arguments
    ---------
     position : 

     reference : 

    """
    def __init__(self,
                 id=None,
                 position=None,
                 reference=None,
                 **kwargs):
        self.id=id
        self.position=position
        self.reference=reference


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = SequencePosition()
        if 'position' in json_obj:
            obj.position = json_obj['position']
        if 'reference' in json_obj:
            obj.reference = json_obj['reference']
        return obj

class SequenceLocation(BioObject):
    """
    SequenceLocation

    Superclass: BioObject

    Arguments
    ---------
     begin : 

     end : 

    """
    def __init__(self,
                 id=None,
                 begin=None,
                 end=None,
                 **kwargs):
        super(SequenceLocation, self).__init__(id, **kwargs)
        self.begin=begin
        self.end=end


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = SequenceLocation()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        if 'taxon' in json_obj:
            obj.taxon = Taxon.from_json(json_obj['taxon'])
        if 'end' in json_obj:
            obj.end = SequencePosition.from_json(json_obj['end'])
        if 'begin' in json_obj:
            obj.begin = SequencePosition.from_json(json_obj['begin'])
        return obj

class Seq(BioObject):
    """
    Seq

    Superclass: BioObject

    Arguments
    ---------
     alphabet : 

         one of: DNA, RNA or AA

     residues : 

         string representing sequence of residues

     md5checksum : 

         checksum

     seqlen : 

         length of sequence

    """
    def __init__(self,
                 id=None,
                 alphabet=None,
                 residues=None,
                 md5checksum=None,
                 seqlen=None,
                 **kwargs):
        super(Seq, self).__init__(id, **kwargs)
        self.alphabet=alphabet
        self.residues=residues
        self.md5checksum=md5checksum
        self.seqlen=seqlen


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Seq()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        if 'taxon' in json_obj:
            obj.taxon = Taxon.from_json(json_obj['taxon'])
        if 'residues' in json_obj:
            obj.residues = json_obj['residues']
        if 'alphabet' in json_obj:
            obj.alphabet = json_obj['alphabet']
        if 'md5checksum' in json_obj:
            obj.md5checksum = json_obj['md5checksum']
        if 'seqlen' in json_obj:
            obj.seqlen = json_obj['seqlen']
        return obj

class SequenceFeature(BioObject):
    """
    SequenceFeature

    Superclass: BioObject

    Arguments
    ---------
     locations : 

     seq : 

     homology_associations : 

    """
    def __init__(self,
                 id=None,
                 locations=None,
                 seq=None,
                 homology_associations=None,
                 **kwargs):
        super(SequenceFeature, self).__init__(id, **kwargs)
        self.locations=locations
        self.seq=seq
        self.homology_associations=homology_associations


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = SequenceFeature()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        if 'taxon' in json_obj:
            obj.taxon = Taxon.from_json(json_obj['taxon'])
        if 'homology_associations' in json_obj:
            obj.homology_associations = [Association.from_json(x) for x in json_obj['homology_associations']]
        if 'seq' in json_obj:
            obj.seq = Seq.from_json(json_obj['seq'])
        if 'locations' in json_obj:
            obj.locations = [SequenceLocation.from_json(x) for x in json_obj['locations']]
        return obj

class Gene(BioObject):
    """
    Gene

    Superclass: BioObject

    Arguments
    ---------
     phenotype_associations : 

         phenotypes associated with alterations of gene

     disease_associations : 

         diseases associated with alterations of gene

     homology_associations : 

         orthology and paralogy assocations for this gene

     function_associations : 

         GO assocations for wild type gene

     genotype_associations : 

         genotypes in which this gene is altered

    """
    def __init__(self,
                 id=None,
                 phenotype_associations=None,
                 disease_associations=None,
                 homology_associations=None,
                 function_associations=None,
                 genotype_associations=None,
                 **kwargs):
        super(Gene, self).__init__(id, **kwargs)
        self.phenotype_associations=phenotype_associations
        self.disease_associations=disease_associations
        self.homology_associations=homology_associations
        self.function_associations=function_associations
        self.genotype_associations=genotype_associations


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Gene()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        if 'taxon' in json_obj:
            obj.taxon = Taxon.from_json(json_obj['taxon'])
        if 'homology_associations' in json_obj:
            obj.homology_associations = [Association.from_json(x) for x in json_obj['homology_associations']]
        if 'phenotype_associations' in json_obj:
            obj.phenotype_associations = [Association.from_json(x) for x in json_obj['phenotype_associations']]
        if 'genotype_associations' in json_obj:
            obj.genotype_associations = [Association.from_json(x) for x in json_obj['genotype_associations']]
        if 'function_associations' in json_obj:
            obj.function_associations = [Association.from_json(x) for x in json_obj['function_associations']]
        if 'disease_associations' in json_obj:
            obj.disease_associations = [Association.from_json(x) for x in json_obj['disease_associations']]
        return obj

class GeneProduct(BioObject):
    """
    GeneProduct

    Superclass: BioObject

    Arguments
    ---------
     genes : 

    """
    def __init__(self,
                 id=None,
                 genes=None,
                 **kwargs):
        super(GeneProduct, self).__init__(id, **kwargs)
        self.genes=genes


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = GeneProduct()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        if 'taxon' in json_obj:
            obj.taxon = Taxon.from_json(json_obj['taxon'])
        if 'genes' in json_obj:
            obj.genes = [Gene.from_json(x) for x in json_obj['genes']]
        return obj

class Transcript(BioObject):
    """
    Transcript

    Superclass: BioObject

    Arguments
    ---------
     genes : 

    """
    def __init__(self,
                 id=None,
                 genes=None,
                 **kwargs):
        super(Transcript, self).__init__(id, **kwargs)
        self.genes=genes


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Transcript()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        if 'taxon' in json_obj:
            obj.taxon = Taxon.from_json(json_obj['taxon'])
        if 'genes' in json_obj:
            obj.genes = [Gene.from_json(x) for x in json_obj['genes']]
        return obj

class Genotype(BioObject):
    """
    Genotype

    Superclass: BioObject

    Arguments
    ---------
     phenotype_associations : 

     disease_associations : 

     gene_associations : 

     variant_associations : 

    """
    def __init__(self,
                 id=None,
                 phenotype_associations=None,
                 disease_associations=None,
                 gene_associations=None,
                 variant_associations=None,
                 **kwargs):
        super(Genotype, self).__init__(id, **kwargs)
        self.phenotype_associations=phenotype_associations
        self.disease_associations=disease_associations
        self.gene_associations=gene_associations
        self.variant_associations=variant_associations


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Genotype()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        if 'taxon' in json_obj:
            obj.taxon = Taxon.from_json(json_obj['taxon'])
        if 'disease_associations' in json_obj:
            obj.disease_associations = [Association.from_json(x) for x in json_obj['disease_associations']]
        if 'gene_associations' in json_obj:
            obj.gene_associations = [Association.from_json(x) for x in json_obj['gene_associations']]
        if 'variant_associations' in json_obj:
            obj.variant_associations = [Association.from_json(x) for x in json_obj['variant_associations']]
        if 'phenotype_associations' in json_obj:
            obj.phenotype_associations = [Association.from_json(x) for x in json_obj['phenotype_associations']]
        return obj

class Allele(Genotype):
    """
    Allele

    Superclass: Genotype

    Arguments
    ---------
    """
    def __init__(self,
                 id=None,
                 **kwargs):
        super(Allele, self).__init__(id, **kwargs)


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Allele()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        if 'taxon' in json_obj:
            obj.taxon = Taxon.from_json(json_obj['taxon'])
        if 'disease_associations' in json_obj:
            obj.disease_associations = [Association.from_json(x) for x in json_obj['disease_associations']]
        if 'gene_associations' in json_obj:
            obj.gene_associations = [Association.from_json(x) for x in json_obj['gene_associations']]
        if 'variant_associations' in json_obj:
            obj.variant_associations = [Association.from_json(x) for x in json_obj['variant_associations']]
        if 'phenotype_associations' in json_obj:
            obj.phenotype_associations = [Association.from_json(x) for x in json_obj['phenotype_associations']]
        return obj

class MolecularComplex(BioObject):
    """
    MolecularComplex

    Superclass: BioObject

    Arguments
    ---------
     genes : 

    """
    def __init__(self,
                 id=None,
                 genes=None,
                 **kwargs):
        super(MolecularComplex, self).__init__(id, **kwargs)
        self.genes=genes


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = MolecularComplex()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        if 'taxon' in json_obj:
            obj.taxon = Taxon.from_json(json_obj['taxon'])
        if 'genes' in json_obj:
            obj.genes = [Gene.from_json(x) for x in json_obj['genes']]
        return obj

class Substance(BioObject):
    """
    Substance

    Superclass: BioObject

    Arguments
    ---------
     target_associations : 

     inchi : 

     inchi_key : 

     smiles : 

    """
    def __init__(self,
                 id=None,
                 target_associations=None,
                 inchi=None,
                 inchi_key=None,
                 smiles=None,
                 **kwargs):
        super(Substance, self).__init__(id, **kwargs)
        self.target_associations=target_associations
        self.inchi=inchi
        self.inchi_key=inchi_key
        self.smiles=smiles


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = Substance()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        if 'taxon' in json_obj:
            obj.taxon = Taxon.from_json(json_obj['taxon'])
        if 'inchi' in json_obj:
            obj.inchi = [x for x in json_obj['inchi']]
        if 'smiles' in json_obj:
            obj.smiles = [x for x in json_obj['smiles']]
        if 'target_associations' in json_obj:
            obj.target_associations = [Association.from_json(x) for x in json_obj['target_associations']]
        if 'inchi_key' in json_obj:
            obj.inchi_key = [x for x in json_obj['inchi_key']]
        return obj

class PhylogeneticNode(NamedObject):
    """
    PhylogeneticNode

    Superclass: NamedObject

    Arguments
    ---------
     feature : 

     parent_id : 

     event : 

     branch_length : 

    """
    def __init__(self,
                 id=None,
                 feature=None,
                 parent_id=None,
                 event=None,
                 branch_length=None,
                 **kwargs):
        super(PhylogeneticNode, self).__init__(id, **kwargs)
        self.feature=feature
        self.parent_id=parent_id
        self.event=event
        self.branch_length=branch_length


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = PhylogeneticNode()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        if 'event' in json_obj:
            obj.event = json_obj['event']
        if 'feature' in json_obj:
            obj.feature = BioObject.from_json(json_obj['feature'])
        if 'parent_id' in json_obj:
            obj.parent_id = json_obj['parent_id']
        if 'branch_length' in json_obj:
            obj.branch_length = json_obj['branch_length']
        return obj

class PhylogeneticTree(NamedObject):
    """
    PhylogeneticTree

    Superclass: NamedObject

    Arguments
    ---------
    """
    def __init__(self,
                 id=None,
                 **kwargs):
        super(PhylogeneticTree, self).__init__(id, **kwargs)


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = PhylogeneticTree()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        return obj

class ClinicalIndividual(NamedObject):
    """
    ClinicalIndividual

    Superclass: NamedObject

    Arguments
    ---------
    """
    def __init__(self,
                 id=None,
                 **kwargs):
        super(ClinicalIndividual, self).__init__(id, **kwargs)


    """
    Create an object from a json representation
    """
    def from_json(json_obj={}):
        obj = ClinicalIndividual()
        if 'synonyms' in json_obj:
            obj.synonyms = [SynonymPropertyValue.from_json(x) for x in json_obj['synonyms']]
        if 'id' in json_obj:
            obj.id = json_obj['id']
        if 'label' in json_obj:
            obj.label = json_obj['label']
        if 'categories' in json_obj:
            obj.categories = [x for x in json_obj['categories']]
        return obj

