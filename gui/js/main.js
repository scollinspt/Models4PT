/* DAGitty - a browser-based software for causal modelling and analysis
*   Copyright (C) 2010-2022 Johannes Textor
* 
*   This program is free software; you can redistribute it and/or
*   modify it under the terms of the GNU General Public License
*   as published by the Free Software Foundation; either version 2
*   of the License, or (at your option) any later version.
* 
*   This program is distributed in the hope that it will be useful,
*   but WITHOUT ANY WARRANTY; without even the implied warranty of
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*   GNU General Public License for more details.
* 
*   You should have received a copy of the GNU General Public License
*   along with this program; if not, write to the Free Software
*   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA. */

console.log("main.js is loaded and running");


var GUI = {
	view_mode : "DAG",
	highlight_causal : true,
	highlight_biasing : true,
	highlight_ancestors : true,
	highlight_puredirect : false,
	allow_intermediate_adjustment : true,
	activate_path_style : function( s, b ){
		var sty = Models4PT.stylesheets.default.style
		if( b ) {
			if(sty[s+"path_inactive"] ){
				sty[s+"path"] = sty[s+"path_inactive"];
				delete sty[s+"path_inactive"];
			}
			displayShow("legend_"+s);
		} else {
			sty[s+"path_inactive"] = sty[s+"path"];
			delete sty[s+"path"];
			displayHide("legend_"+s);
		}
		Models4PTControl && Models4PTControl.redraw();
	},
	activate_node_style : function( s, b ){
		var sty = Models4PT.stylesheets.default.style
		if( b ) {
			if(sty[s+"node_inactive"] ){
				sty[s+"node"] = sty[s+"node_inactive"];
				delete sty[s+"node_inactive"];
			}
		} else {
			sty[s+"node_inactive"] = sty[s+"node"];
			delete sty[s+"node"];
		}
	},
	set_highlight_biasing : function( b ){
		this.activate_path_style( "biasing", b );
	},
	set_highlight_causal : function( b ){
		this.activate_path_style( "causal", b );
	},
	set_highlight_puredirect : function( b ){
		this.activate_path_style( "puredirect", b );
	},
	set_highlight_ancestors : function( b ){
		this.highlight_ancestors = b;
		_.each(["confounder","anexposure","anoutcome"],function(n){
			this.activate_node_style( n, b );
		},this);
		b ? displayShow("legend_ancestors") : displayHide("legend_ancestors");
		Models4PTControl && Models4PTControl.redraw();
	},
	set_view_mode : function( vm ){
		let vmel = document.getElementById( "dagview_"+vm )
		vmel.checked ||= true
		Models4PTControl && Models4PTControl.setViewMode( vm );
	},
	set_bias_mode : function( bm ){
		Models4PTControl && Models4PTControl.setBiasMode( bm );		
	},
	refresh_variable_status : function(){
		var vid = document.getElementById("variable_id").value
		document.getElementById("variable_label").innerText = vid
		document.getElementById("variable_exposure").checked = Model.dag.isSource(vid)
		document.getElementById("variable_outcome").checked = Model.dag.isTarget(vid)
		document.getElementById("variable_selected").checked = Model.dag.isSelectedNode(vid)
		document.getElementById("variable_adjusted").checked = Model.dag.isAdjustedNode(vid)
		document.getElementById("variable_unobserved").checked = Model.dag.isLatentNode( vid )
	},
	set_variable_status : function( n, stat ){
		var vid = document.getElementById("variable_id").value
		if( stat ){
			Models4PTControl && Models4PTControl.setVertexProperty( vid, n )
		} else {
			Models4PTControl && Models4PTControl.unsetVertexProperty( vid, n )
		}
	},
	set_style : function( s ){
		Models4PT.stylesheets.default = Models4PT.stylesheets[s]
		var sty = Models4PT.stylesheets.default.style
		document.getElementById("highlight_ancestral").checked = typeof(sty["confoundernode_inactive"]) === "undefined";
		document.getElementById("highlight_ancestral").checked ? displayShow("legend_ancestors") : displayHide("legend_ancestors");
		
		document.getElementById("highlight_causal").checked = typeof(sty["causalpath_inactive"]) === "undefined";
		document.getElementById("highlight_causal").checked ? displayShow("legend_causal") : displayHide("legend_causal");
		
		document.getElementById("highlight_biasing").checked = typeof(sty["biasingpath_inactive"]) === "undefined";
		document.getElementById("highlight_biasing").checked ? displayShow("legend_biasing") : displayHide("legend_biasing");
		
		document.getElementById("highlight_puredirect").checked = typeof(sty["puredirectpath_inactive"]) === "undefined";
		_.each(["biasingpath","causalpath","exposure","latentnode","lnode","mnode","other",
			"outcome","rnode","adjustednode"],function(n){
			document.getElementById("li"+n).src="images/legend/"+s+"/"+n+".png"
		},this);
		Models4PTControl.setStyle( s )
	}
};


/**
 * Some convenience functions.
 * 
 **/

function displayArrow( id, on ){
	if( document.getElementById("a_"+id) ){
		document.getElementById("a_"+id).src =  "images/arrow-" + (on?"down":"right") + ".png";
	}
}
function displayShow( id ){
	var e = document.getElementById(id);
	if( !e ){ 
		return;
	}
	if( e.tagName == "SPAN" ){
		e.style.display = "inline";
	} else {
		e.style.display = "block";
	}
	displayArrow( id, true );
}
function displayHide( id ){
	var e = document.getElementById(id);
	if( !e ){ 
		return;
	}
	e.style.display = "none";
	displayArrow( id, false );
}
function displayToggle( id ){
	var on = true;
	if( document.getElementById(id).style.display == "block" ){
		document.getElementById(id).style.display = "none";
		on = false;
	} else {
		document.getElementById(id).style.display = "block";
	}
	displayArrow( id, on );
}

function menuOpen( id ){
	for( var i = 0 ; i < GUI.menus.length ; i ++ ){
		if( GUI.menus[i] != id ){
			displayHide( "menu_"+GUI.menus[i] )
		} else {
			displayShow( "menu_"+id )
		}
	}
}

function menuToggle( id ){
	for( var i = 0 ; i < GUI.menus.length ; i ++ ){
		if( GUI.menus[i] != id ){
			displayHide( "menu_"+GUI.menus[i] )
		} else {
			displayToggle( "menu_"+id )
		}
	}
}

function nl2br (str, is_xhtml) {
    var breakTag = (is_xhtml || typeof is_xhtml === 'undefined') ? '<br />' : '<br>';
    return (str + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + breakTag + '$2');
}

function msg( t ){
	Models4PTControl.getView().openAlertDialog( t );
}

function how( t ){
	msg( t );
	displayHide('menu_howto')
}

function setsToHTML( sets ){
	if( sets.length > 0 ){
		var msas_html = [];
		for( var i = 0 ; i < sets.length ; i ++ ){
			msas_html[i] = "{";
			var ids = _.pluck(sets[i],'id').sort();
			for( var j = 0 ; j < ids.length ; j ++ ){
				if( j > 0 ){
					msas_html[i] += ", ";
				}
				if( Model.dag.isAdjustedNode( ids[j] ) ){
					msas_html[i] += "<strong>"+ids[j]+"</strong>";
				} else {
					msas_html[i] += ids[j];
				}
			}
			msas_html[i] += "}";
		} 
		return "<ul><li>"+msas_html.sort().join("</li><li>")+"</li></ul>";
	} else {
		return "";
	}
}

function msgP( t ){
	let r = document.createElement("p")
	r.innerText = t
	return r
}

function msgWarnP( t ){
	let r = msgP( t )
	r.className = "warning"
	return r
}

function msgOKP( t ){
	let r = msgP( t )
	r.className = "assurance"
	return r
}


/** 
 * Functions that compute things.
 */

function causalEffectEstimates( effect_type ){
	/*if( Model.dag.getSelectedNodes().length > 0 ){
		displayCausalMsg("I cannot determine causal effects for DAGs with selection nodes."); return 
	}*/
	if( GraphAnalyzer.containsCycle( Model.dag ) ){
		displayCausalMsg("Can't determine causal effects for cyclic models."); return 
	}
	switch( effect_type ){
		case "adj_total" :
			GUI.set_bias_mode('normal')
			displayAdjustmentInfo("total"); break
		case "adj_direct" :
			GUI.set_bias_mode('direct')
			displayAdjustmentInfo("direct"); break
		case "adj_causalodds" :
			GUI.set_bias_mode('causalodds')
			displayAdjustmentInfo("causalodds"); break
		case "instrument" :
			GUI.set_bias_mode('normal')
			displayInstrumentInfo(); break
		case "treeid" :
			GUI.set_bias_mode('normal')
			displayTreeIDInfo(); break
	}
}

/** Updates the "adjustment" UI component. The variable "kind" can be one of
	"total" or "direct". */
	
function msasToHtml( msas ){
	let r = null;
	if( msas.length > 0 ){
		let msas_html = [];
		for( let i = 0 ; i < msas.length ; i ++ ){
			msas_html[i] = "";
			let ids = _.pluck(msas[i],'id').sort();
			for( let j = 0 ; j < ids.length ; j ++ ){
				if( j > 0 ){
					msas_html[i] += ", ";
				}
				if( Model.dag.isAdjustedNode( ids[j] ) ){
					msas_html[i] += ids[j];
				} else {
					msas_html[i] += ids[j];
				}
			}
		}
		r = document.createElement("ul")
		for( let e of msas_html.sort() ){
			let ee = document.createElement("li")
			ee.innerText = e
			r.appendChild( ee )
		}
	}
	return r
}

function displayCausalMsg( wh ){	
	document.getElementById("causal_effect").innerHTML 
		= "<p>"+wh+"</p>";
}

function displayAdjustmentInfo( kind ){	
	let g = Model.dag

	let adjusted_nodes = g.getAdjustedNodes();
	let note_adjustment = "";

	let exposures = _.pluck(g.getSources(),'id').sort()
	let outcomes = _.pluck(g.getTargets(),'id').sort()
	let adjusted = _.pluck(g.getAdjustedNodes(),'id').sort()
	let selected = _.pluck(g.getSelectedNodes(),'id').sort()

	let exposures_list = _.pluck(g.getSources(),'id').sort()
	let outcomes_list = _.pluck(g.getTargets(),'id').sort()

	let tgt_el = document.getElementById("causal_effect")
	tgt_el.replaceChildren()

	if( exposures_list.length > 0 ){
		tgt_el.appendChild( msgP( "Exposure"+(exposures.length > 1?"s: ":": ")+exposures_list.join(",") ) )
	} else {
		tgt_el.appendChild( msgWarnP( "No exposure defined." ) )
	}

	if( outcomes_list.length > 0 ){
		tgt_el.appendChild( msgP( "Outcome"+(outcomes.length > 1?"s: ":": ")+outcomes_list.join(",") ) ) 
	} else {
		tgt_el.appendChild( msgWarnP( "No outcome defined." ) )
	}

	/* All adjustment types need at least one exposure and outcome. */
	if( exposures.length == 0 || outcomes.length == 0 ){
		return
	}

	/* For non-total effects, we need exactly one exposure and/or outcome. */
	if( kind == "causal odds ratio" ){
		if( exposures.length > 1 ){
			tgt_el.appendChild( msgWarnP( "Multiple exposures defined." ) )		
		}
		if( outcomes.length > 1 ){
			tgt_el.appendChild( msgWarnP( "Multiple outcomes defined." ) )		
		}
		return
	}

	if( selected.length > 0 ){
		let selected_el = document.createElement( "p" )
		selected_el.innerText = "Selected: "+selected.join(",")
		tgt_el.appendChild( selected_el )
		if( kind == "direct" ){
			tgt_el.appendChild( msgWarnP("Selection nodes not supported for direct effects." ) )
			return
		}
	} 
	
	if( kind == "causalodds" ){
		if( selected.length == 0 ){
			tgt_el.appendChild( msgWarnP("Selection node not defined." ) )
			return
		}
		if( selected.length > 1 ){
			tgt_el.appendChild( msgWarnP("There must be a unique selection node." ) )
			return
		}
	}

	if( adjusted.length > 0 ){
		let adjusted_el = document.createElement( "p" )
		adjusted_el.innerText = "Adjusted: "+adjusted.join(",")
		tgt_el.appendChild( adjusted_el )
	}

	let f = "isAdjustmentSet"
	if( kind == "direct" ){
		f = "isAdjustmentSetDirectEffect"
	}
	if( kind == "causalodds" ){
		f = "isAdjustmentSetCausalOddsRatio"
	}

	if( GraphAnalyzer[f]( g ) ){
		if( adjusted.length == 0 ){
			tgt_el.appendChild( msgOKP( "No open biasing paths." ) )
		} else {
			tgt_el.appendChild( msgOKP( "Correctly adjusted." ) )
		}
	} else {
		if( adjusted.length == 0 ){
			tgt_el.appendChild( msgWarnP( "Biasing paths are open." ) )
		} else {
			tgt_el.appendChild( msgWarnP( "Incorrectly adjusted." ) )
		}
	}

	/** From here on, list adjustment sets.
	  * This currently only works for total and direct effects. Also, we cannot list
	  * adjustment sets yet if there is a selection node.
	  */

	if( !["total","direct"].includes( kind ) || selected.length > 0 ){ return } 

	let adjustment_list_el = document.createElement( "p" )

	tgt_el.appendChild( adjustment_list_el )

	if( adjusted_nodes.length > 0 ){
		note_adjustment = " containing "+_.pluck(adjusted_nodes,'id').sort().join(", ");
	}
	
	let showMsas = function( t, msas, note_a, el ){
		if( msas.length == 1 && msas[0].length == 0 ){
			el.innerText = "No adjustment is necessary to estimate the "+t+" of "+
					_.pluck(Model.dag.getSources(),'id').join(",") +
					" on " + _.pluck(Model.dag.getTargets(),'id').join(",") + ".";
			return
		}
		let msas_html = msasToHtml( msas );
		if( msas_html ){
			el.innerText = "Minimal sufficient adjustment sets "+note_a+" for estimating the "+t+" of "
				+ _.pluck(Model.dag.getSources(),'id').join(",") 
				+ " on " + _.pluck(Model.dag.getTargets(),'id').join(",") + ": "
			el.after( msas_html )
		} else {
			el.innerText = "No adjustment sets found.";
		}
	};

	if( kind == "total" ){
		showMsas( "total effect",
			GraphAnalyzer.listMsasTotalEffect( g ), note_adjustment, adjustment_list_el );
	}
	
	if( kind == "direct" ){
		showMsas( "direct effect",
			GraphAnalyzer.listMsasDirectEffect( g ), note_adjustment, adjustment_list_el );
	}
}


function ivsToHtml( ivs ){
	if( ivs.length > 0 ){
		var ivs_html = [];
		for( var i = 0 ; i < ivs.length ; i ++ ){
			ivs_html[i] = ivs[i][0].id
			if( ivs[i][1].length > 0 ){
				ivs_html[i] += " | "+_.pluck(ivs[i][1],'id').join(', ');
			}
		} 
		return "<ul><li>"+ivs_html.sort().join("</li><li>")+"</li></ul>";
	} else {
		return "";
	}
}

function displayInstrumentInfo(){
	if( Model.dag.getSources().length != 1 || 
		Model.dag.getTargets().length != 1 ){
		document.getElementById("causal_effect").innerHTML = "<p>Instrumental variable identification is only supported for a single exposure and a single outcome.</p>"
		return
	}
	var ivs = GraphAnalyzer.conditionalInstruments( Model.dag )
	if( ivs === false ){
		document.getElementById("causal_effect").innerHTML = "<p>Instrumental variable identification is not supported for this kind of DAG.</p>"
		return
	}
	if( ivs.length == 0 ){
		document.getElementById("causal_effect").innerHTML = "<p>There are no instruments or conditional instruments in this DAG.</p>"
		return
	}
	document.getElementById("causal_effect").innerHTML = "<p>Instruments and conditional instruments:</p>"
		+ ivsToHtml( ivs )
}

function getVertexParent(v){
	var pa = Model.dag.getVertex(v).getParents()
	if (pa.length != 1) return "(invalid parents)";
	return pa[0].id
}
function missingCyclesToString(missingCycles) {
	if ( missingCycles.length == 0 ) return
	if ( missingCycles.length == 1 )
		return "missing cycle " + missingCycles[0].join(", ")
	return "missing cycles " + _.map(missingCycles, function(c){return c.join(", ")}).join(" and ")
}
function showTreeFASTP(id) {
	var q = getVertexParent(id)
	var res = window.lastTreeIDResults.results[id][0]
	var msg =  "The effect λ"+q+id+" of "+q + " on "+id+" is given by: \n"
	if (res.propagate) {
		var j = id
		var i = res.propagate
		var p = getVertexParent(i)
		msg += "( λ"+p+i+" σ"+p+j + " - σ"+i+j+ " ) / ( λ"+p+i+" σ"+p+q + " - σ" + i + q+")\n"
		msg += "\n which is equivalent to \n"
	}
	msg += res.fastp.join("\n\nOR\n")
	function alen(a){ return a ? a.length : 0 }
	if (alen(res.missingCycles) + alen(res.oldPropagatedMissingCycles) + alen(res.oldMissingCycles) + alen(res.propagatedMissingCycles) > 0) {
		msg += "\n\n\nThe calculation used cycles: \n"
		var mc = []
		_.map(["missingCycles", "propagatedMissingCycles", "oldMissingCycles"], function(mcid){ 
			if (res[mcid]) mc.push(missingCyclesToString(res[mcid])) 
		})
		msg += mc.join(", ")
	}
	if (res.propagatePath){
		msg += "\n\n\n"
		msg += "The solution propagated from:"+res.propagatePath.join("<->")
		if (res.missingCycles) {
			msg += "\n(One cycle was found that yielded 2 possible solutions which propagated here. Another cycle was found which elimated one of the solutions, yielding one unique solution.) "
		}
	}
	alert(msg)
}
function treeIDResultsToHtml( tid ){
	window.lastTreeIDResults = tid
	function resultsToHtmlForKID(kID){
		var r = "";
		_.each(tid.results, function edgeIdToHtml(v, k){
			if (v[0].fastp.length != kID) return
			//console.log(v[0])
			if (v[0].fastp) {
				r += "<li>Effect of "+getVertexParent(k)+" on " + k + ":<br><a href='javascript:showTreeFASTP( \""+k+"\")'>"
				if (v[0].instrument) {
					r += "instrumental variable " + v[0].instrument
				}
				if (v[0].propagate && (!v[0].missingCycles || !v[0].propagatedMissingCycles) ) {
					r += "propagate from " + v[0].propagate
				}
				if (v[0].missingCycles) {
					r += missingCyclesToString(v[0].missingCycles)
					if (v[0].propagate && v[0].propagatedMissingCycles ) {
						r += "<br>and " + missingCyclesToString(v[0].propagatedMissingCycles) + " propagated from " + v[0].propagate
					}
				}
				r += "</a></li>"
			}
		})
		return r
	}
	
	var temp = resultsToHtmlForKID(1)
	var r = ""
	if (temp) r += "<p>Identifiable edges:</p><ul>" + temp + "</ul>"
	var temp = resultsToHtmlForKID(2)
	if (temp) r += "<p><font color='red'>≤ 2-Identifiable</font> edges:</p><ul>" + temp + "</ul>"
	return r
}

function displayTreeIDInfo(){
	var warnings = []
	if( Model.dag.getSources().length != 0 || 
		Model.dag.getTargets().length != 0 ){
		warnings = ["<p>Exposure and outcome nodes are ignored for TreeID."+
			"Instead, TreeID tests identifiability of every direct effect (path coefficient) "+
			"simultaneously.</p>"]
		document.getElementById("causal_effect").innerHTML = "<p><font color='red'>"+warnings[0]+"</font></p>"
	}
	var tid
	try {
		tid = GraphAnalyzer.treeID( Model.dag )
	} catch (e) {
		alert(e)
		document.getElementById("causal_effect").innerHTML = "<p>"+e+"</p>"
		return
	}
	var out = treeIDResultsToHtml( tid )
	if (tid.warnings) warnings = warnings.concat(tid.warnings)
	_.each(warnings, function(w){ out += "<p><font color='red'>"+w+"</font></p>" })
	document.getElementById("causal_effect").innerHTML = out
}


function displayImplicationInfo( full ){
	var imp;
	var more_link = false;
	if( full ){
		imp = GraphAnalyzer.listMinimalImplications( Model.dag );
	}
	else{
		imp = GraphAnalyzer.listMinimalImplications( Model.dag , 10 );
	}
	if( imp.length > 0 ){
		var imp_html = "<p>The model implies the following conditional independences: </p><ul><li>";
		var n = 0;
		for( var i = 0 ; i < imp.length ; i ++ ){
			for( j = 0 ; j < imp[i][2].length ; j ++ ){
				if( full || ++n < 10 ){
					if( i > 0 || j > 0 ) imp_html += "</li><li>";
					imp_html += imp[i][0]+" &perp; "+imp[i][1];
					if( imp[i][2][j].length > 0 ){
						imp_html += " | "+_.pluck(imp[i][2][j],'id').sort().join(", ");
					} 
				}  else {
					more_link = true;
				}
			}
		}
		imp_html += "</ul>";
		document.getElementById("testable_implications").innerHTML = imp_html +
			(more_link?'<p><a href="javascript:void(0)" onclick="displayImplicationInfo( true )">Show all ...</a></p>':'')
	} else {
		document.getElementById("testable_implications").replaceChildren( msgP( "Either the model does not imply any conditional independencies "
			+" or the implied ones are untestable due to unobserved variables.") )
	}
}

function exportTikzCode(){
	Models4PTControl.getView().openHTMLDialog( 
		"<textarea style=\"width:80%\" rows=\"10\">"+
		"% This code uses the tikz package\n"+
		"\\begin{tikzpicture}\n"+
		 GraphSerializer.toTikz( Model.dag, 3 ) +
		"\\end{tikzpicture}"+
		"</textarea>", "OK"
	)
}

/** updates the "summary" component */ 
function displayGeneralInfo(){
	var cycle = GraphAnalyzer.containsCycle( Model.dag );
	if( cycle ){
		displayShow("info_cycle");
		displayHide("info_summary");
		document.getElementById("info_cycle").innerHTML = "<p class=\"warning\">Model contains cycle: "+cycle+"</p>";
	} else {
		if ( _.some(Model.dag.getEdges(), function(e) { return e.directed == Graph.Edgetype.Undirected; } ) )
			cycle = GraphAnalyzer.containsSemiCycle(Model.dag);
		if (cycle) {
			displayShow("info_cycle");
			displayHide("info_summary");
			document.getElementById("info_cycle").innerHTML = "<p class=\"warning\">Model contains semi-cycle: "+cycle+"</b></p>";
		} else {
			displayHide("info_cycle");
			displayShow("info_summary");
			document.getElementById("info_exposure").innerHTML = _.pluck(Model.dag.getSources(),'id').join(",");
			document.getElementById("info_outcome").innerHTML = _.pluck(Model.dag.getTargets(),'id').join(",");
			document.getElementById("info_covariates").innerHTML = Model.dag.getNumberOfVertices()-Model.dag.getSources().length
			-Model.dag.getTargets().length;
			document.getElementById("info_frontdoor").innerHTML = Model.dag.countPaths();
			// $("info_backdoor").innerHTML = dag_ancestor_pair_graph.countPaths();      
		}
	}
	/*$("path_information").innerHTML = nl2br("Closed paths:<br/>"+dag_ancestor_graph.listClosedPaths()
	*         + "<br/><br/>Open paths:<br/>"+dag_ancestor_pair_graph.listPathPairs(),true);*/
}

function loadDAGFromTextData(){
	Model.dag = GraphParser.parseGuess( document.getElementById("adj_matrix").value );
	if( !Model.dag.hasCompleteLayout() ){
		var layouter = new GraphLayouter.Spring( Model.dag );
		layouter.layout();
	}
	Models4PTControl.setGraph( Model.dag  );
	displayHide("model_refresh");
	document.getElementById("adj_matrix").style.backgroundColor="#fff";
}

function generateSpringLayout(){
	var layouter = new GraphLayouter.Spring( Model.dag );
	_.each(Model.dag.edges,function(e){delete e["layout_pos_x"];delete e["layout_pos_y"]})
	layouter.layout();
	Models4PTControl.setGraph( Model.dag ); // trigges to refresh the rendering
};

function loadExample( nr ){
	nr = parseInt( nr )
	if( examples[nr].d ){
		document.getElementById("adj_matrix").value = examples[nr].d 
	} else {
		document.getElementById("adj_matrix").value = 
			examples[nr].v+"\n\n"+examples[nr].e;
	}
	loadDAGFromTextData();
}

function newModel(){
	document.getElementById("adj_matrix").value = 'dag { bb="0,0,1,1" }'
	loadDAGFromTextData();
}
function newModel2(ename){
	if( ename === null ){ return false; }
	ename = (""+ename).trim()
	if( ename == "" ){ return false; }
	Models4PTControl.getView().openPromptDialog(
		"Please enter name of outcome variable","",function(s){ 
			newModel3(ename,s) } )
	return true;
}
function newModel3(ename,oname){
	if( oname == null ){ return false; }
	oname = (""+oname).trim()
	if( oname == "" || ename == oname ){ return false; }
	document.getElementById("adj_matrix").value = ename+" E @0,0\n"+oname+" O @1,1\n\n"+ename+" "+oname
	loadDAGFromTextData()
	Models4PTControl.getView().closeDialog()
}

function supportsSVG() {
	return document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#BasicStructure", "1.1") ||
	document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#BasicStructure", "1.0");
};

// The exportPDF function submits a request to the backend to export the graph as a PDF.
// This functionality is disabled temporarily while transitioning to localStorage.
/*
function exportPDF(){
	if( supportsSVG() ){
		document.getElementById("exportformsvg").value = document.getElementById("canvas").innerHTML;
		document.getElementById("exportform").action = "https://"+hostName()+ "/pdf/batik-pdf.php";
		document.getElementById("exportform").submit();
	}
}
*/

function exportBitmap( format ){
	if( !format ) format = "png"
	const svgElement = document.querySelector('svg');
	const w = svgElement.getBoundingClientRect().width;
	const h = svgElement.getBoundingClientRect().height;
	svgElement.setAttribute("width", w)
	svgElement.setAttribute("height", h)
	const svgString = new XMLSerializer().serializeToString(svgElement);
	const blob = new Blob([svgString], { type: 'image/svg+xml' });
	const img = new Image();
	const url = URL.createObjectURL(blob);
	img.onload=function(){
		const canv = document.createElement("canvas")
		const ctx = canv.getContext("2d")
		ctx.imageSmoothingQuality = "high"
		canv.width = 2*w	
		canv.height = 2*h
		ctx.fillStyle = "white"
		ctx.fillRect( 0, 0, 2*w, 2*h )	
		ctx.drawImage(img, 0, 0, w, h, 0, 0, 2*w, 2*h )
		URL.revokeObjectURL( url )
		const uri = canv.toDataURL( 'image/'+format )
		const a = document.createElement( 'a' );
		document.body.appendChild( a );
    		a.style = 'display: none';
	   	a.href = uri
		a.download="models4pt-model."+format
		a.click()
		window.URL.revokeObjectURL( uri )
		document.body.removeChild( a )
	}
	img.src = url
}

function exportPNG(){
	exportBitmap( "png" )
}

function exportJPEG(){
	exportBitmap( "jpeg" )
}


function exportSVG(){
	const svgElement = document.querySelector('svg');
	svgElement.setAttribute("xmlns", "http://www.w3.org/2000/svg");
	const w = svgElement.getBoundingClientRect().width;
	const h = svgElement.getBoundingClientRect().height;
	svgElement.setAttribute("width", w)
	svgElement.setAttribute("height", h)
	const preface = '<?xml version="1.0" standalone="no"?>\r\n';
	const svgString = svgElement.outerHTML
	const blob = new Blob([preface,svgString], {type:"image/svg+xml;charset=utf-8"} );
	const url = URL.createObjectURL(blob);
	const a = document.createElement( 'a' );
    	a.style = 'display: none';
	a.href = url
	a.download="models4pt-model.svg"
	document.body.appendChild( a );
	a.click()
	document.body.removeChild( a )
	window.URL.revokeObjectURL( url )
}
// The hostName function dynamically determines the backend URL based on the environment.
// Currently disabled as we are transitioning to localStorage for save/load functionality.
/*
function hostName(){
	switch( window.location.hostname ){
		case "models4pt.net":
			return "models4pt.net";
		case "models4pt.concebo.eu":
			return "models4pt.concebo.eu";
		case "www.models4pt.com":
			return "www.models4pt.com";
	}
	return "models4pt.com";
}
*/

/** Dialogues for online model storage */

function networkFailMsg(){
	msg(
	 "A network error occurred when trying to perform this function. "+
	 "If you are using a downloaded Models4PT version, this is likely "+
	 "due to Browser security settings. Try again using the online "+
	 "version of Models4PT." )
}

function getModelIdFromURL( url ){
	return url.substring(url.indexOf('.net/m')+'.net/m'.length)
}


var publishwindow
function saveOnlineForm(){
	if( publishwindow && !publishwindow.closed ){
		publishwindow.setModelCode( Model.dag.toString() )
		publishwindow.focus()
	} else {
		publishwindow = window.open( "publish.html", "net_models4pt_publishwindow" )
		publishwindow.onload = function(){ publishwindow.setModelCode( Model.dag.toString() ) }
	}
}



// New localStorage-based version	
async function loadOnline(url) {
	var graphid = getModelIdFromURL(url); // Extract the graph ID from the URL
	try {
		// Retrieve the model from localStorage using the graph ID
		const modelData = localStorage.getItem(graphid);
		if (!modelData) {
			alert("Model not found in localStorage. Please check the ID and try again.");
			return;
			}
	
		// Parse the stored JSON data
		const modelsyntax = JSON.parse(modelData);
	
		// Update the UI and render the DAG
		Models4PTControl.getView().closeDialog();
		document.getElementById("adj_matrix").value = modelsyntax.g;
		Model.uniqid = graphid; // Optional: track the graph ID
		loadDAGFromTextData(); // Render the graph
	} catch (err) {
		alert("Failed to load model. Please try again.");
		console.log(err);
	}
}
	
// Updated loadOnlineForm function for localStorage:
// This version prompts the user for a Graph ID instead of a URL and loads the model from localStorage.
function loadOnlineForm() {
    Models4PTControl.getView().openPromptDialog(
        "Enter the Graph ID",
        "exampleGraph123", // Example placeholder
        function (graphID) {
            if (!graphID) {
                alert("Graph ID is required to load a model.");
                return;
            }
            loadOnline(graphID); // Call the updated loadOnline function
        }
    );
}




		// ----------------------------
// Save and Load Functionality
// ----------------------------

function saveModel(graphid, modelData) {
    const currentTimestamp = new Date().toISOString(); // Get the current date and time
    const modelWithTimestamp = {
        syntax: modelData,
        timestamp: currentTimestamp,
    };

    localStorage.setItem(graphid, JSON.stringify(modelWithTimestamp)); // Save with timestamp
    console.log(`Model '${graphid}' saved at ${currentTimestamp}.`);
}



function saveModelPrompt() {
    // Prompt the user for a unique Graph ID
    const graphid = prompt("Enter a unique ID for your graph:");
    if (!graphid) {
        alert("Graph ID is required to save the model.");
        return;
    }

    // Retrieve the model data from the DOM (e.g., from an element with id "adj_matrix")
    const modelData = document.getElementById("adj_matrix").value; // Replace with actual model data source
    if (!modelData) {
        alert("No model data found to save.");
        return;
    }

    console.log("Saving model with ID:", graphid, "and data:", modelData); // Log before saving
    saveModel(graphid, modelData); // Call saveModel to handle the actual saving
}


function loadModel(graphid) {
    try {
        // Retrieve the model data from localStorage
        const modelData = localStorage.getItem(graphid);
        if (!modelData) {
            alert("Model not found. Please check the ID and try again.");
            return;
        }

        // Parse the model data from JSON
        const parsedData = JSON.parse(modelData);

        // Update the UI (e.g., populate the adjacency matrix input)
        const adjMatrixElement = document.getElementById("adj_matrix");
        if (!adjMatrixElement) {
            console.error("Element with ID 'adj_matrix' not found.");
            alert("Failed to load model. Please check the UI setup.");
            return;
        }
        adjMatrixElement.value = parsedData.syntax;

        // Call a function to render the DAG (assumes loadDAGFromTextData exists in your codebase)
        if (typeof loadDAGFromTextData === "function") {
            loadDAGFromTextData();
        } else {
            console.warn("loadDAGFromTextData function not found. DAG rendering may not work.");
        }

        console.log(`Successfully loaded model: ${graphid}`, parsedData); // Debugging log
    } catch (error) {
        console.error("Error loading model:", error);
        alert("Failed to load model. Please try again.");
    }
}


function loadModelPrompt() {
    // First, display the list of saved models
    viewSavedModels();

    // Then, prompt the user to select a model
    const graphid = prompt("Enter the number corresponding to the model you want to load:");
    if (!graphid) {
        alert("Model ID is required to load a model.");
        return;
    }

    // Load the selected model
    loadModel(graphid);
}


// ----------------------------
// View Saved Models
// ----------------------------
function viewSavedModels() {
    // Retrieve all saved models from localStorage and sort alphabetically
    const savedModels = Object.keys(localStorage).sort();

    // If no models are saved, notify the user
    if (savedModels.length === 0) {
        alert("No models found in local storage.");
        return;
    }

    // Create a list with timestamps
    let modelList = "Saved Models (Alphabetical Order):\n\n";
    savedModels.forEach((key, index) => {
        // Parse the saved data to include timestamps if stored
        const modelData = JSON.parse(localStorage.getItem(key));
        const timestamp = modelData.timestamp || "Unknown Date";

        modelList += `${index + 1}. ${key} (Last Modified: ${timestamp})\n`;
    });

    // Display the list to the user
    const selectedModelIndex = prompt(
        `${modelList}\nEnter the number of the model you want to load:`
    );

    if (selectedModelIndex) {
        const modelIndex = parseInt(selectedModelIndex, 10) - 1;
        if (modelIndex >= 0 && modelIndex < savedModels.length) {
            const modelID = savedModels[modelIndex];
            loadModel(modelID); // Load the selected model
        } else {
            alert("Invalid selection. Please try again.");
        }
    }
}

// ----------------------------
// Delete Saved Models
// ----------------------------

function deleteModel(graphid) {
    localStorage.removeItem(graphid);
    console.log(`Model '${graphid}' deleted from localStorage.`);
    alert(`Model '${graphid}' has been deleted.`);
}


function deleteModelPrompt() {
    // Get all keys from localStorage and sort alphabetically
    const savedModels = Object.keys(localStorage).sort();

    // If no models are saved, notify the user
    if (savedModels.length === 0) {
        alert("No models found in local storage.");
        return;
    }

    // Create a list with timestamps
    let modelList = "Saved Models (Alphabetical Order):\n\n";
    savedModels.forEach((key, index) => {
        // Parse the saved data to include timestamps if stored
        const modelData = JSON.parse(localStorage.getItem(key));
        const timestamp = modelData?.timestamp || "Unknown Date";

        modelList += `${index + 1}. ${key} (Last Modified: ${timestamp})\n`;
    });

    // Prompt the user to select a model to delete
    const selectedModelIndex = prompt(
        `${modelList}\nEnter the number of the model you want to delete:`
    );

    if (selectedModelIndex) {
        const modelIndex = parseInt(selectedModelIndex, 10) - 1;
        if (modelIndex >= 0 && modelIndex < savedModels.length) {
            const modelID = savedModels[modelIndex];
            const confirmDelete = confirm(`Are you sure you want to delete '${modelID}'?`);
            if (confirmDelete) {
                deleteModel(modelID); // Call deleteModel to handle deletion
            }
        } else {
            alert("Invalid selection. Please try again.");
        }
    }
}



