WIKIDOT.modules.NewSiteModule={};WIKIDOT.modules.NewSiteModule.listeners={next:function(c){var b=OZONE.utils.formToArray($("new-site-form"));b.action="NewSiteAction";b.event="createSite";OZONE.ajax.requestModule(null,b,WIKIDOT.modules.NewSiteModule.callbacks.next);var a=new OZONE.dialogs.WaitBox();a.content="Creating site...";a.show()}};WIKIDOT.modules.NewSiteModule.callbacks={next:function(d){if(d.status=="form_errors"){OZONE.dialog.cleanAll();var b="The data you have submitted contains following errors:<ul>";var g=d.formErrors;for(var c in g){b+="<li>"+g[c]+"</li>"}b+="</ul>";$j("#new-site-form-errors").html(b).show();OZONE.visuals.scrollTo("new-site-box");return}if(!WIKIDOT.utils.handleError(d)){return}var a=new OZONE.dialogs.SuccessBox();a.content="New site successfully created!";a.show();try{_gaq.push(["_trackPageview","/_analytics_goal/newsite"])}catch(f){}setTimeout("window.location.href='http://"+d.siteUnixName+"."+URL_DOMAIN+"'",1000)}};