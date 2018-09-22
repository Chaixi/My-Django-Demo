$('a[type=button]').on('click', function() {
			/* Act on the event */
			var data_index = $(this).attr('data-index');
			var data_index_id = $(this).attr('data-index').toString().split('_')[1];
			console.log(data_index_id);
			console.log($(this).attr('data-index'));
			var source = $(this).attr('data-index').toString().split('_')[0];
			var id = $(this).attr('data-index').toString().split('_')[1];

//			去除new标签
            $('span[data-index='+source+'_'+id+']').text("");
//            alert("111");
//            $('a[data-index='+source+'_'+id+']').attr("class", "visited");
            $('a[data-index='+source+'_'+id+']').css("color", "#d9534f");

			$.ajax({
				url: '/news_detail',
				type: 'POST',
				dataType: 'json',
				data: {
				    "id": id,
				    "source": source,
				    },
				success: function(data){
				    LoadModalData(data)
					<!--console.log(data);-->
				},
			});

			$('#myModal').modal('show');
		});

		function LoadModalData(data) {
//		    console.log(data);
			// 加载消息标题
			$('#myModalLabel').text(data['title']);
			$('#myModalLabel').attr('href', data['link']);

			<!--加载发布时间、消息来源-->
			$('#release_time').text("发布时间："+data['release_time'].toString().split("T")[0]);
			$('#source').text("来源："+data['source']);

			// 加载消息内容，先清空
			$('#newsContent').empty();
			$('#newsContent').append('<p>'+data['content'].replace('\r\n','</p><p>')+'</p>');

			// 加载消息图片，先清空，拼接,3张图片一行
			$('#newsPic').empty();
//			console.log(data['imgs']);
			imgLink = data['imgs'].toString().split(";");
			imgContent = '';
//			console.log(imgLink);
			for (var i = 0; i < imgLink.length-1; i++) {
				if ( i%3 == 0 ) {
				    if( i != 0 )
				    {
				        imgContent += '</div>'
				    }
					imgContent += '<div class="row" style="text-align: right;">';
				}
				imgContent += '<div class="col-md-4"><a href="'+imgLink[i]+'" class="thumbnail" target="_blank"><img src="'+imgLink[i]+'" alt="80*80">'+'</a></div>';

			}
			imgContent += '</div>';
//			console.log(imgContent);

			$('#newsPic').append(imgContent);
		};