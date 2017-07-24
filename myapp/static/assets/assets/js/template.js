//slideshow
var tpj=jQuery;

      var revapi11;
      tpj(document).ready(function() {
        if(tpj("#slideshow").revolution == undefined){
          revslider_showDoubleJqueryError("#slideshow");
        }else{
          revapi11 = tpj("#slideshow").show().revolution({
            sliderType:"standard",
            // jsFileLocation:"{{ url_for('static', filename='assets/assets/js')}}",
            sliderLayout:"fullscreen",
            dottedOverlay:"none",
            delay:3000,
            navigation: {
              keyboardNavigation:"off",
              keyboard_direction: "horizontal",
              mouseScrollNavigation:"off",
              mouseScrollReverse:"default",
              onHoverStop:"off",
              arrows: {
                style:"gyges",
                enable:true,
                hide_onmobile:true,
                hide_under:480,
                hide_onleave:false,
                tmp:'',
                left: {
                  h_align:"left",
                  v_align:"center",
                  h_offset:20,
                  v_offset:0
                },
                right: {
                  h_align:"right",
                  v_align:"center",
                  h_offset:20,
                  v_offset:0
                }
              }
            },
            responsiveLevels:[1240,1024,778,480],
            visibilityLevels:[1240,1024,778,480],
            gridwidth:[1240,1024,778,480],
            gridheight:[698,500,500,500],
            lazyType:"smart",
            parallax: {
              type:"scroll",
              origo:"slidercenter",
              speed:400,
              levels:[5,10,15,20,25,30,35,40,-15,-20,-25,-30,-35,-40,-45,55],
              type:"scroll",
              disable_onmobile:"on"
            },
            shadow:0,
            spinner:"spinner2",
            stopLoop:"off",
            stopAfterLoops:-1,
            stopAtSlide:-1,
            shuffle:"off",
            autoHeight:"off",
            fullScreenAutoWidth:"off",
            fullScreenAlignForce:"off",
            fullScreenOffsetContainer: "",
            fullScreenOffset: "",
            disableProgressBar:"on",
            hideThumbsOnMobile:"off",
            hideSliderAtLimit:0,
            hideCaptionAtLimit:0,
            hideAllCaptionAtLilmit:0,
            debugMode:false,
            fallbacks: {
              simplifyAll:"off",
              nextSlideOnWindowFocus:"off",
              disableFocusListener:false,
            }
          });
        }
      });  /*ready*/

//slogan
var tpj=jQuery;
      var revapi22;
      tpj(document).ready(function() {
        if(tpj("#slogan").revolution == undefined){
          revslider_showDoubleJqueryError("#slogan");
        }else{
          revapi22 = tpj("#slogan").show().revolution({
            sliderType:"hero",
            // jsFileLocation:"{{ url_for('static', filename='assets/assets/js')}}",
            sliderLayout:"fullwidth",
            dottedOverlay:"none",
            delay:0,
            navigation: {
            },
            responsiveLevels:[1240,1024,778,480],
            visibilityLevels:[1240,1024,778,480],
            gridwidth:[1240,1024,778,480],
            gridheight:[120,120,150,180],
            lazyType:"none",
            shadow:0,
            spinner:"off",
            autoHeight:"off",
            disableProgressBar:"on",
            hideThumbsOnMobile:"off",
            hideSliderAtLimit:0,
            hideCaptionAtLimit:0,
            hideAllCaptionAtLilmit:0,
            debugMode:false,
            fallbacks: {
              simplifyAll:"off",
              disableFocusListener:false,
            }
          });
        }
      });  /*ready*/

//discover
var tpj=jQuery;

      var revapi19;
      tpj(document).ready(function() {
        if(tpj("#discover").revolution == undefined){
          revslider_showDoubleJqueryError("#discover");
        }else{
          revapi19 = tpj("#discover").show().revolution({
            sliderType:"standard",
            // jsFileLocation:"public/assets/js/",
            // jsFileLocation:"{{ url_for('static', filename='assets/assets/js')}}",
            sliderLayout:"fullwidth",
            dottedOverlay:"none",
            delay:0,
            navigation: {
              onHoverStop:"off",
            },
            viewPort: {
              enable:true,
              outof:"wait",
              visible_area:"80%"
            },
            responsiveLevels:[1240,1024,778,480],
            visibilityLevels:[1240,1024,778,480],
            gridwidth:[1240,1024,778,480],
            gridheight:[815,690,547,1692],
            lazyType:"single",
            shadow:0,
            spinner:"spinner2",
            stopLoop:"off",
            stopAfterLoops:-1,
            stopAtSlide:-1,
            shuffle:"off",
            autoHeight:"off",
            disableProgressBar:"on",
            hideThumbsOnMobile:"off",
            hideSliderAtLimit:0,
            hideCaptionAtLimit:0,
            hideAllCaptionAtLilmit:0,
            debugMode:false,
            fallbacks: {
              simplifyAll:"off",
              nextSlideOnWindowFocus:"off",
              disableFocusListener:false,
            }
          });
          var is_safari = (navigator.userAgent.indexOf('Safari') != -1 && navigator.userAgent.indexOf('Chrome') == -1);

          revapi19.bind("revolution.slide.onloaded",function (e) {
            var npe = document.getElementsByClassName("nopointerevent");
            for (var i=0;i<npe.length;i++) {
              npe[i].parentNode.parentNode.parentNode.style.pointerEvents = "none";
              npe[i].parentNode.parentNode.parentNode.style.zIndex = 100;
            }
                                   
            jQuery('.ddd_mousebox').on('mousemove',function(e) {       
              var sto = revapi19.offset(),
              dim = this.getBoundingClientRect(),
              tpos = jQuery(this.parentNode.parentNode.parentNode).position(),
              pos = {top:e.pageY-sto.top-tpos.top,left:e.pageX-tpos.left},
              perc = {wp:(pos.left/dim.width)-0.5, hp:(pos.top/dim.height)-0.5};
              getOverlaps(this);
              punchgs.TweenLite.to(this.overlapps,0.4,{force3D:"true",overwrite:"auto",transformOrigin:"50% 50% 100%", z:"300px",rotationY:0-((perc.wp)*5),rotationX:((perc.hp)*5),zIndex:30});
              punchgs.TweenLite.set(this.parentNode.parentNode.parentNode,{zIndex:10});
              if (is_safari)
                punchgs.TweenLite.to(this,0.4,{force3D:"true",overwrite:"auto",z:"10px",transformOrigin:"50% 50%", rotationY:0-((perc.wp)*10),rotationX:((perc.hp)*10)});
              else
                punchgs.TweenLite.to(this,0.4,{force3D:"true",overwrite:"auto",z:"10px",transformOrigin:"50% 50%", rotationY:0-((perc.wp)*10),rotationX:((perc.hp)*10),boxShadow:"0 50px 100px rgba(15,20,40,0.35),0 20px 45px rgba(15,20,40,0.35)"});
            });

            jQuery('.ddd_mousebox').on('mouseleave',function(e) {
              punchgs.TweenLite.set(this.parentNode.parentNode.parentNode,{zIndex:5});
              punchgs.TweenLite.to(this,0.5,{force3D:"true",overwrite:"auto",z:"0px",transformOrigin:"50% 50%", rotationY:0,rotationX:0,boxShadow:"0,0,0,0 rgba(0,0,0,0)"});
              punchgs.TweenLite.to(this.overlapps,0.5,{force3D:"true",z:"0px",overwrite:"auto",transformOrigin:"50% 50% 100%", rotationY:0,rotationX:0});
            });
     
          });
                                   
          function getOverlaps(el) {
            if (el.overlapps == undefined) {
              el.overlapps = [];
              var jel = jQuery(el),
              jpel = jQuery(el.parentNode.parentNode.parentNode),
              pos_e = jpel.position();
              pos_e.bottom = jel.height()+pos_e.top;
              pos_e.right = jel.width()+pos_e.left;                                   

              revapi19.find('.tp-caption').each(function() {

                var cel = jQuery(this.parentNode.parentNode.parentNode),
                pos_cel = cel.position();                       

                if (this!==el && pos_cel.top>=pos_e.top && pos_cel.top<=pos_e.bottom && pos_cel.left>=pos_e.left && pos_cel.left<=pos_e.right)  el.overlapps.push(cel);
              });
            } 
          }        
        }
      });  /*ready*/

//footer
var tpj=jQuery;

      var revapi23;
      tpj(document).ready(function() {
        if(tpj("#footer").revolution == undefined){
          revslider_showDoubleJqueryError("#footer");
        }else{
          revapi23 = tpj("#footer").show().revolution({
            sliderType:"hero",
            // jsFileLocation:"{{ url_for('static', filename='assets/assets/js')}}",
            sliderLayout:"fullwidth",
            dottedOverlay:"none",
            delay:9000,
            navigation: {
            },
            responsiveLevels:[1240,1024,778,480],
            visibilityLevels:[1240,1024,778,480],
            gridwidth:[1240,1024,778,480],
            gridheight:[50,50,50,50],
            lazyType:"none",
            shadow:0,
            spinner:"off",
            autoHeight:"off",
            disableProgressBar:"on",
            hideThumbsOnMobile:"off",
            hideSliderAtLimit:0,
            hideCaptionAtLimit:0,
            hideAllCaptionAtLilmit:0,
            debugMode:false,
            fallbacks: {
              simplifyAll:"off",
              disableFocusListener:false,
            panZoomDisableOnMobile:"on",
            }
          });
        }
      });  /*ready*/