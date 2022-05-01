/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jeongkpa <jeongkpa@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/04/25 01:51:29 by jeongkpa          #+#    #+#             */
/*   Updated: 2022/04/25 13:30:02 by jeongkpa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../includes/ft_printf.h"

static void	ft_parser(char c, va_list ap, int *ret)
{
	if (c == 'c')
	{
		ft_putchar_fd((char) va_arg(ap, int), 1);
		*ret += 1;
	}
	else if (c == 's')
		ft_putstr_and_cnt((char *) va_arg(ap, char *), ret);
	else if (c == 'p')
		ptr2hex((unsigned long int) va_arg(ap, unsigned long int), ret);
	else if (c == 'd')
		ft_decimal2b10((int) va_arg(ap, int), ret);
	else if (c == 'i')
		ft_int2b10((int) va_arg(ap, int), ret);
	else if (c == 'u')
		ft_uint2b10((unsigned int) va_arg(ap, unsigned int), ret);
	else if (c == 'x')
		nbr_ui2hex((unsigned int) va_arg(ap, unsigned int), ret, 'x');
	else if (c == 'X')
		nbr_ui2hex((unsigned int) va_arg(ap, unsigned int), ret, 'X');
	else if (c == '%')
	{
		ft_putchar_fd('%', 1);
		*ret += 1;
	}
}

int	ft_printf(const char *str, ...)
{
	va_list		ap;
	size_t		cnt;
	int			ret;

	cnt = 0;
	ret = 0;
	va_start(ap, str);
	while (str[cnt])
	{
		if (str[cnt] == '%')
		{
			cnt++;
			ft_parser(str[cnt], ap, &ret);
		}
		else
		{
			ft_putchar_fd(str[cnt], 1);
			ret++;
		}
		cnt++;
	}
	va_end(ap);
	return (ret);
}