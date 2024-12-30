# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:24:14 2024

@author: Mijn-PC
"""




from pygenomeviz import GenomeViz

name, genome_size = "OX457036.1:2000000-3000000",  3000000
cds_list = ((2087020, 2087265, -1), (2089471, 2089899, 1), (2106048,2106398,-1), (2108840,2109808,-1), (2112894,2113442, -1), ( 2121930, 2122163,1), (2257178,2267675,-1), (2310931,2315817,1 ) )

gv = GenomeViz()
track = gv.add_feature_track(name, genome_size)
for idx, cds in enumerate(cds_list, 1):
    start, end, strand = cds
    track.add_feature(start, end, strand, label=f"CDS{idx:02d}")

gv.savefig("example01.png")



gv = GenomeViz()
gv.set_scale_xticks(ymargin=0.5)


track = gv.add_feature_track("OX457036.1", (2087020, 2109808))
track.add_sublabel()


# Add features to track
track.add_feature(2087020,  2087265, -1)
track.add_feature(2089471, 2089899, 1, fc="blue")    
track.add_feature(2106048, 2106398, -1, fc="lime")
track.add_feature(2108840, 2109808, -1, fc="magenta", lw=1.0)
fig = gv.plotfig()

gv.savefig("example01.png")




from pygenomeviz import GenomeViz
from pygenomeviz.parser import Genbank
from pygenomeviz.utils import load_example_genbank_dataset


gbk = Genbank("OX457036.1.genbank")

gv = GenomeViz()
gv.set_scale_bar(ymargin=0.05)

track = gv.add_feature_track(gbk.name, gbk.genome_length)
#track = gv.add_feature_track(gbk.name, (2000000,3000000))
track.add_sublabel()

features = gbk.extract_features()
track.add_features(features, plotstyle="bigarrow", label="bigarrow", fc="red", lw=0.05)

gv.savefig("terr.genbank.png")

gv.savefig_html("OX457036.1.html")







from pygenomeviz import GenomeViz
from pygenomeviz.parser import Genbank
from pygenomeviz.utils import load_example_genbank_dataset


gv = GenomeViz(
    fig_track_height=0.7,
    feature_track_ratio=20  
)


gbk = Genbank("part1.genbank")
track = gv.add_feature_track(gbk.name, (2000000,2259000))
features = gbk.extract_features()
track.add_features(features)


#track.add_genbank_features(gbk, facecolor="limegreen", linewidth=0.5, arrow_shaft_ratio=1.0)
gv.savefig("example05.png")



gv.savefig("example05.png")


from dna_features_viewer import GraphicFeature, GraphicRecord

from dna_features_viewer import BiopythonTranslator
graphic_record = BiopythonTranslator().translate_record("lumter3mb.gb")
ax, _ = graphic_record.plot(figure_width=10)
ax.figure.savefig("custom_bopython_translator.png")

# add fea


from dna_features_viewer import GraphicFeature, GraphicRecord
features=[
    GraphicFeature(start=20, end=265, strand=-1, color="#ffd700",
                   label="Lumbricus rubellus AJ299434.1 gene g5"),
    GraphicFeature(start=471, end=899, strand=1, color="#ffd700",
                   label="Lamperta planeri OZ078387.2 gene g6"),
    GraphicFeature(start=106048, end=106398, strand=-1, color="#ffd700",
                   label="Mus musculus AC121136.11 gene g8"),    
    GraphicFeature(start=108840, end=109808, strand=-1, color="#ffd700",
                   label="Candidozyma auris CP157508.1 gene g11"),
    GraphicFeature(start=112894, end=113442, strand=-1, color="#ffd700",
                   label="Ixodes scapularis G-protein coupled receptor dmsr; XM_029969893.4 gene g13") ,     
    GraphicFeature(start=121930, end=122163, strand=1, color="#ffd700",
                   label="Melanogrammus aeglefinus emb OZ180142.1 gene 14 ") ,
    GraphicFeature(start=267178, end=267675, strand=-1, color="#ffd700",
                 label=" Earthworm (L.terrestris) extracellular globin chain c gene, complete cds; gb J05161.1 LUMHBC gene g24"),  
    GraphicFeature(start=310931, end=315817, strand=-1, color="#ffd700",
                 label=" Zymobacter palmae IAM14233 DNA, complete genome;dbj|AP018933.1	 gene25 ") ,                 
    GraphicFeature(start=417427, end=418269, strand=1, color="#ffd700",
                 label="Hylaeus volcanicus  mRNA;XM_054124195.1 gene  35"),
    GraphicFeature(start=435738, end=435962, strand=1, color="#ffd700",
             	label="Mus musculus BAC clone RP23-95F15  gene  37"),    
    GraphicFeature(start=438078, end=438413, strand=-1, color="#ffd700",
             	label="emb  OE003277.1	  gene  38"),
    GraphicFeature(start=527938, end=528267, strand=1, color="#ffd700",
             	label="Earthworm(L.terrestris) extracellular globin chain c gene, complete cds;J05161.1 LUMHBC  gene 40 "),
    
    GraphicFeature(start=577242, end=577547, strand=-1, color="#ffd700",
             	label="Helobdella robusta hypothetical protein mRNA	 gene 43 " ),
    
    GraphicFeature(start=577242, end=577547, strand=-1, color="#ffd700",
             	label="Periplaneta americana carbonic anhydrase beta (CAHbeta) XM_069820523.1, gene46 " ),
    
    GraphicFeature(start=597827, end=599035, strand=-1, color="#ffd700",
             	label="Loxodonta africana zinc finger protein 252-like (LOC100666328), gene47 " ),
    
    GraphicFeature(start=600509, end=600898, strand=-1, color="#ffd700",
             	label="Bos taurus isolate Dominette_000065F KX592814.1 gene48" ),    
        
    GraphicFeature(start=625618, end=625986, strand=1, color="#ffd700",
             	label="Earthworm (L.terrestris) extracellular globin chain c gene, complete cds, gene54" ),
    
    GraphicFeature(start=650957, end=651178, strand=-1, color="#ffd700",
             	label="Dictyostelium discoideum AX4 hypothetical protein mRNA XM_637462.1 gene56" ),
    
        
    GraphicFeature(start=650957, end=651178, strand=-1, color="#ffd700",
             	label="Dictyostelium discoideum AX4 hypothetical protein mRNA XM_637462.1 gene56" ),
        
    GraphicFeature(start=654466, end=654759, strand=1, color="#ffd700",
             	label=":Rattus norvegicus  LOC134482949  gene57" ),
        
    GraphicFeature(start=678908, end=679186, strand=-1, color="#ffd700",
             	label="Melanogrammus aeglefinus gene63" )
    
    
]

record = GraphicRecord(sequence_length=679186, features=features)
record.plot(figure_width=5)

ax, _ =record.plot(figure_width=4)

#ax.figure.set_size_inches(12, 8)
ax.figure.savefig("custom_bopython-feature.png")

##  bokenh


from dna_features_viewer import BiopythonTranslator
from bokeh.resources import CDN
from bokeh.embed import file_html

record = GraphicRecord(sequence_length=528267, features=features)
plot = record.plot_with_bokeh(figure_width=8)

with open("2-3mb-terrsetris.html", "w+") as f:
    f.write(file_html(plot, CDN, "Featuresfor2-3mbchr1LumbricusTerrestris"))

