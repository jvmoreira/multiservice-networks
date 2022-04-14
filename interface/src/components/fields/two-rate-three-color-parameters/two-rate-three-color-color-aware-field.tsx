import React, { ChangeEvent, ReactElement, useCallback, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { ChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorColorAwareField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const isColorAwareEnabled = useMemo(() => {
    return Boolean(twoRateThreeColorParameters.color_aware);
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorColorAware = useSetNfvTeFunctionParameter('color_aware', setTwoRateThreeColorParameters);

  const onTwoRateThreeColorColorAwareChangeHandler = useCallback((evt: ChangeEvent<HTMLInputElement>) => {
    setTwoRateThreeColorColorAware(evt.target.checked ? '1': undefined);
  }, [setTwoRateThreeColorColorAware]);

  return (
    <FormInput
      label="Color Aware"
      name="color-aware"
      type="checkbox"
      checked={isColorAwareEnabled}
      onChange={onTwoRateThreeColorColorAwareChangeHandler as ChangeHandler}
    />
  );
}
